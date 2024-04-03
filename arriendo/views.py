from django.shortcuts import render, redirect
import calendar
from .models import *
from .forms import *
#from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
import json
from django.core.paginator import Paginator
from django.db.models import Sum, Count
from django.db.models.functions import ExtractMonth
from django.http import JsonResponse
from django.db.models import Avg
from reportlab.pdfgen import canvas



# Vista principal
def index (request):
    return render(request, 'base/index.html')

# Vista login
#def login (request):
    template_name = 'registration/login.html'  # 


#VISTA VER MAQUINARIA
@login_required
def maquinaria(request):
    #Trae datos de los modelos
    maquinarias = Maquinaria.objects.all()
    arriendos = Arriendos.objects.values_list('maquina_arriendo__id_m', flat=True).distinct()
    
    #Verifica si la maquina esta en un registro de arriendos  ##Mejorar funcion
    for maquinaria in maquinarias:
        if maquinaria.id_m in arriendos:
            maquinaria.estado = "No Disponible"
            maquinaria.save()
            
    # Obtén los criterios de búsqueda desde la URL
    m_filter = request.GET.get('m_filter')

    # Aplica los filtros según los criterios de búsqueda
    if m_filter:
        maquinarias = maquinarias.filter(nombre_m__icontains=m_filter)
            
    context = {'maquinarias': maquinarias}
    #Añade la paginacion
    paginator = Paginator(maquinarias, 4)  # Muestra 4 elementos por página
    page = request.GET.get('page')
    maq_pag = paginator.get_page(page)
    
    return render(request, 'maquinaria/maquinaria_index.html', {'maquinarias': maq_pag,})


#VISTA AGREGAR MAQUINARIA
@login_required
def agregar_maquinaria (request): 
    formulario_m = MaquinariaForm(request.POST or None, request.FILES or None)
    if formulario_m.is_valid():
        formulario_m.save()
        return redirect('maquinaria')
    return render(request,'maquinaria/agregarmaquinaria.html', {'formulario_m': formulario_m})

@login_required
def eliminar_maquinaria (request, id_m): 
    maquinaria = Maquinaria.objects.get(id_m=id_m)
    maquinaria.delete()
    return redirect('maquinaria')

@login_required
def editar_maquinaria (request, id_m): 
    maquinaria = Maquinaria.objects.get(id_m=id_m)
    formulario_m = MaquinariaForm(request.POST or None, request.FILES or None, instance=maquinaria)
    if formulario_m.is_valid() and request.POST:
        formulario_m.save()
        return redirect('maquinaria')
    return render(request,'maquinaria/editar_maquinaria.html', {'formulario_m': formulario_m})
        

#VISTA CLIENTES
@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    # Obtén los criterios de búsqueda desde la URL
    cliente_filter = request.GET.get('cliente_filter')

    # Aplica los filtros según los criterios de búsqueda
    if cliente_filter:
        clientes = clientes.filter(rut_empresa=cliente_filter)
    #Paginacion
    paginator = Paginator(clientes, 4)  # 4 registros por página

    page = request.GET.get('page')
    clientes_paginados = paginator.get_page(page)

    return render(request, 'cliente/clientes_index.html', {'clientes': clientes_paginados})
 
 #AGREGAR CLIENTE
@login_required
def agregar_cliente (request): 
    formulario_cl = ClienteForm(request.POST or None, request.FILES or None)
    if formulario_cl.is_valid():
        formulario_cl.save()
        return redirect('clientes')
    return render(request, 'cliente/agregar_cliente.html', {'formulario_cl': formulario_cl})

#EDITAR CLIENTE
@login_required
def editar_cliente (request, id_cliente): 
    clientes = Cliente.objects.get(id_cliente=id_cliente)
    formulario_cl = ClienteForm(request.POST or None, request.FILES or None, instance = clientes)
    if formulario_cl.is_valid() and request.POST:
            formulario_cl.save()
            return redirect('clientes')
    return render(request, 'cliente/editar_cliente.html', {'formulario_cl': formulario_cl})

#ELIMINAR CLIENTE
@login_required
def eliminar_cliente (request, id_cliente): 
    clientes = Cliente.objects.get(id_cliente=id_cliente)
    clientes.delete()
    return redirect('clientes')
    
#VISTA  ARRIENDO
@login_required
def arriendo (request):
    #Trae todos los datos del modelo
    arriendos_list = Arriendos.objects.all()
    
    # Obtén los criterios de búsqueda desde la URL
    maquina = request.GET.get('maquina')
    fecha_inicio = request.GET.get('fecha_inicio')

    # Aplica los filtros según los criterios de búsqueda
    if maquina:
        arriendos_list = arriendos_list.filter(maquina_arriendo__nombre_m__icontains=maquina)
    if fecha_inicio:
        arriendos_list = arriendos_list.filter(fecha_inicio=fecha_inicio)
    #Añade la paginacion
    paginator = Paginator(arriendos_list, 4)  # Muestra 4 elementos por página
    page = request.GET.get('page')
    arriendos = paginator.get_page(page)

    return render(request, 'arriendo/ver_arriendo.html', {'arriendos': arriendos,})

#ISTA AGREAGAR ARRIENDO
@login_required
def agregar_arriendo (request):
    formulario_arr = ArriendoForm(request.POST or None, request.FILES or None)
    if formulario_arr.is_valid():
        formulario_arr.save()
        return redirect('arriendo')
    return render(request, 'arriendo/agregar_arriendo.html', {'formulario_arr': formulario_arr})

#ELIMINAR ARRIENDO
@login_required
def eliminar_arriendo (request, id_arriendo): 
    arriendo = Arriendos.objects.get(id_arriendo=id_arriendo)
    arriendo.delete()
    return redirect('arriendo')

#EDITAR ARRIENDO
@login_required
def editar_arriendo (request, id_arriendo): 
    arriendo = Arriendos.objects.get(id_arriendo=id_arriendo)
    formulario_arr = ArriendoForm(request.POST or None, request.FILES or None, instance = arriendo)
    if formulario_arr.is_valid() and request.POST:
            formulario_arr.save()
            return redirect('arriendo')
    return render(request, 'arriendo/editar_arriendo.html', {'formulario_arr': formulario_arr})


#Vista Graficos Arriendo
def grafico_arriendos(request):
    # Recopila los datos 
    categorias = Categorias.objects.all()
    datos = []
    for categoria in categorias:
        arriendos_categoria = Arriendos.objects.filter(maquina_arriendo__categoria_m=categoria)
        datos.append({
            "nombre": categoria.nombre_cat,
            "cantidad": arriendos_categoria.count()
        })
    
    # Convierte datos a JSON 
    datos_json = json.dumps(datos)
    
    return render(request, 'graficas/dashboard.html', {'datos': datos_json})


def chart_data2(request):
# Recopilamos los datos
    data = (
        Arriendos.objects.values('maquina_arriendo__categoria_m__nombre_cat')
        .annotate(total_cost=Sum('costo_total'))
    )
    
    labels = [entry['maquina_arriendo__categoria_m__nombre_cat'] for entry in data]
    values = [entry['total_cost'] for entry in data]

    chart_data = {
        'labels': labels,
        'values': values,
    }
    
    return JsonResponse(chart_data, safe=False)

def chart_data(request):
    data = (
        Arriendos.objects.values('maquina_arriendo__categoria_m__nombre_cat')
        .annotate(total_cost=Sum('costo_total'))
    )
    
    labels = [entry['maquina_arriendo__categoria_m__nombre_cat'] for entry in data]
    values = [entry['total_cost'] for entry in data]

   
    chart_data = {
        'labels': labels,
        'values': values,
    }
    return JsonResponse(chart_data, safe=False)


#Grafico numero 3 line chart
# Agrupa los arriendos por mes y calcula el costo total
def chart_data3(request):
    # Obtén los datos del modelo y suma el costo total por mes
    data = (
        Arriendos.objects.values('fecha_inicio__year', 'fecha_inicio__month')
        .annotate(total_cost=Sum('costo_total'))
        .order_by('fecha_inicio__year', 'fecha_inicio__month')
    )

    # Crea una lista con los valores y etiquetas para el gráfico
    values = [entry['total_cost'] for entry in data]
    labels = [calendar.month_name[entry['fecha_inicio__month']] for entry in data]

    chart_data = {
        'labels': labels,
        'values': values,
    }

    return JsonResponse(chart_data)

def duracion_promedio_por_categoria(request):
    data = (
        Maquinaria.objects
        .values('categoria_m__nombre_cat')
        .annotate(promedio_duracion=Avg('arriendos__dias_arriendo'))
    )
    
    labels = [entry['categoria_m__nombre_cat'] for entry in data]
    values = [entry['promedio_duracion'] for entry in data]

    chart_data = {
        'labels': labels,
        'values': values,
    }
    return JsonResponse(chart_data, safe=False)





'''
#def arriendos_chart(request):
    # Obtén los datos de costo total por categoría de maquinaria
    data = Arriendos.objects.values('maquina_arriendo__categoria__nombre').annotate(total_cost=Sum('costo_total'))

    chart_data = []
    for item in data:
        category = item['maquina_arriendo__categoria_m_nombre']
        cost = item['total_cost']
        chart_data.append({'name': category, 'y': cost})

    return JsonResponse(chart_data, safe=False)
    '''
from io import BytesIO
from django.http import HttpResponse
import requests
from django.urls import reverse


from django.http import HttpResponse
from django.shortcuts import render
from PIL import ImageGrab
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import os

def capture_and_create_pdf(request):
    if request.method == 'POST':
        x1 = int(request.POST.get('x1'))
        y1 = int(request.POST.get('y1'))
        x2 = int(request.POST.get('x2'))
        y2 = int(request.POST.get('y2'))

        # Captura la pantalla utilizando las coordenadas proporcionadas
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))

        # Crea un nuevo PDF en un objeto BytesIO
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)

        # Guarda la captura en un archivo temporal
        screenshot_path = '/tmp/screenshot.png'  # Define la ubicación temporal
        screenshot.save(screenshot_path, format="PNG")
        screenshot_width, screenshot_height = screenshot.size

        # Dibuja la captura en el PDF desde el archivo temporal
        pdf.drawImage(screenshot_path, 100, 500, width=screenshot_width, height=screenshot_height)

        # Agrega contenido adicional (texto, gráficos, etc.) al PDF según tus necesidades
        pdf.drawString(100, 300, "Texto adicional")

        # Guarda y cierra el PDF
        pdf.showPage()
        pdf.save()

        # Elimina el archivo temporal
        os.remove(screenshot_path)

        # Configura la respuesta HTTP para descargar el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="captured_chart.pdf"'
        buffer.seek(0)
        response.write(buffer.read())
        buffer.close()

        return response

    return render(request, 'dashboard.html')







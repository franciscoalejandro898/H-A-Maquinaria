from django.shortcuts import render, redirect
from .models import *
from .forms import *
#from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
import json


# Vista principal
def index (request):
    return render(request, 'base/index.html')

# Vista login
#def login (request):
    template_name = 'registration/login.html'  # Ruta a tu plantilla personalizada de inicio de sesión


#VISTA VER MAQUINARIA
@login_required
def maquinaria(request):
    maquinarias = Maquinaria.objects.all()
    arriendos = Arriendos.objects.values_list('maquina_arriendo__id_m', flat=True).distinct()
    
    for maquinaria in maquinarias:
        if maquinaria.id_m in arriendos:
            maquinaria.estado = "No Disponible"
    
    context = {'maquinarias': maquinarias}
    return render(request, 'maquinaria/maquinaria_index.html', context)


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
def clientes (request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/clientes_index.html', {'clientes': clientes})
 
@login_required
def agregar_cliente (request): 
    formulario_cl = ClienteForm(request.POST or None, request.FILES or None)
    if formulario_cl.is_valid():
        formulario_cl.save()
        return redirect('clientes')
    return render(request, 'cliente/agregar_cliente.html', {'formulario_cl': formulario_cl})

@login_required
def editar_cliente (request, id_cliente): 
    clientes = Cliente.objects.get(id_cliente=id_cliente)
    formulario_cl = ClienteForm(request.POST or None, request.FILES or None, instance = clientes)
    if formulario_cl.is_valid() and request.POST:
            formulario_cl.save()
            return redirect('clientes')
    return render(request, 'cliente/editar_cliente.html', {'formulario_cl': formulario_cl})

@login_required
def eliminar_cliente (request, id_cliente): 
    clientes = Cliente.objects.get(id_cliente=id_cliente)
    clientes.delete()
    return redirect('clientes')
    
#VISTA REGISTRAR ARRIENDO
@login_required
def arriendo (request):
    arriendos= Arriendos.objects.all()
    return render(request, 'arriendo/ver_arriendo.html', {'arriendos': arriendos})

@login_required
def agregar_arriendo (request):
    formulario_arr = ArriendoForm(request.POST or None, request.FILES or None)
    if formulario_arr.is_valid():
        formulario_arr.save()
        return redirect('arriendo')
    return render(request, 'arriendo/agregar_arriendo.html', {'formulario_arr': formulario_arr})

@login_required
def eliminar_arriendo (request, id_arriendo): 
    arriendo = Arriendos.objects.get(id_arriendo=id_arriendo)
    arriendo.delete()
    return redirect('arriendo')

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
    # Recopila los datos de la base de datos
    categorias = Categorias.objects.all()
    datos = []
    for categoria in categorias:
        arriendos_categoria = Arriendos.objects.filter(maquina_arriendo__categoria_m=categoria)
        datos.append({
            "nombre": categoria.nombre_cat,
            "cantidad": arriendos_categoria.count()
        })
    
    # Convierte datos a una cadena JSON válida
    datos_json = json.dumps(datos)
    
    return render(request, 'graficas/index_graf.html', {'datos': datos_json})
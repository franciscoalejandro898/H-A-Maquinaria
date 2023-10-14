from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Vista principal
def index (request):
    return render(request, 'base/index.html')

# Vista login
def login (request):
    return render(request, 'base/login.html')

#VISTA MAQUINARIA
#def maquinaria (request):
#    maquinaria = Maquinaria.objects.all()
#    return render(request, 'maquinaria/maquinaria_index.html', {'maquinarias': maquinaria} )

def maquinaria(request):
    maquinarias = Maquinaria.objects.all()
    arriendos = Arriendos.objects.values_list('maquina_arriendo__id_m', flat=True).distinct()
    
    for maquinaria in maquinarias:
        if maquinaria.id_m in arriendos:
            maquinaria.estado = "No Disponible"
    
    context = {'maquinarias': maquinarias}
    return render(request, 'maquinaria/maquinaria_index.html', context)


#vista Agregar Maquinaria
def agregar_maquinaria (request): 
    formulario_m = MaquinariaForm(request.POST or None, request.FILES or None)
    if formulario_m.is_valid():
        formulario_m.save()
        return redirect('maquinaria')
    return render(request,'maquinaria/agregarmaquinaria.html', {'formulario_m': formulario_m})

#VISTA CLIENTES
def clientes (request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/clientes_index.html', {'clientes': clientes})
 
def agregar_cliente (request): 
    formulario_cl = ClienteForm(request.POST or None, request.FILES or None)
    if formulario_cl.is_valid():
        formulario_cl.save()
        return redirect('clientes')
    return render(request, 'cliente/agregar_cliente.html', {'formulario_cl': formulario_cl})

def editar_cliente (request): 
    return render(request, 'cliente/editar_cliente.html')

def eliminar_cliente (request):
    return render(request, 'cliente/eliminar_cliente.html')

#vista Arriendo
def arriendo (request):
    arriendos= Arriendos.objects.all()
    return render(request, 'arriendo/ver_arriendo.html', {'arriendos': arriendos})

def agregar_arriendo (request):
    formulario_arr = ArriendoForm(request.POST or None, request.FILES or None)
    if formulario_arr.is_valid():
        formulario_arr.save()
        return redirect('arriendo')
    return render(request, 'arriendo/agregar_arriendo.html', {'formulario_arr': formulario_arr})


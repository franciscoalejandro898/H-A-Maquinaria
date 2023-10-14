from django.shortcuts import render
from .models import *


# Vista principal
def index (request):
    return render(request, 'base/index.html')

# Vista login
def login (request):
    return render(request, 'base/login.html')

#VISTA MAQUINARIA
def maquinaria (request):
    maquinaria = Maquinaria.objects.all()
    return render(request, 'maquinaria/maquinaria_index.html', {'maquinarias': maquinaria} )

#vista Agregar Maquinaria
def agregar_maquinaria (request): 
    maquinaria = Maquinaria.objects.all()
    return render(request,'maquinaria/agregarmaquinaria.html')

#VISTA CLIENTES
def clientes (request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/clientes_index.html', {'clientes': clientes})
 
def agregar_cliente (request): 
    return render(request, 'cliente/agregar_cliente.html')

def editar_cliente (request): 
    return render(request, 'cliente/editar_cliente.html')

def eliminar_cliente (request):
    return render(request, 'cliente/eliminar_cliente.html')

#vista Arriendo
def arriendo (request):
    arriendos= Arriendos.objects.all()
    return render(request, 'arriendo/ver_arriendo.html', {'arriendos': arriendos})

def agregar_arriendo (request):
    return render(request, 'arriendo/agregar_arriendo.html')


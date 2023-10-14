from django.shortcuts import render


# Vista principal
def index (request):
    return render(request, 'base/index.html')

# Vista login
def login (request):
    return render(request, 'base/login.html')

#vista MAQUINARIA
def maquinaria (request):
    return render(request, 'maquinaria/maquinaria_index.html')

#vista Agregar Maquinaria
def agregar_maquinaria (request): 
    return render(request,'maquinaria/agregarmaquinaria.html')

#VISTA CLIENTES
def clientes (request):
    return render(request, 'cliente/clientes_index.html')

def agregar_cliente (request): 
    return render(request, 'cliente/agregar_cliente.html')

def editar_cliente (request): 
    return render(request, 'cliente/editar_cliente.html')

def eliminar_cliente (request):
    return render(request, 'cliente/eliminar_cliente.html')

#vista Arriendo
def arriendo (request):
    return render(request, 'arriendo/ver_arriendo.html')

def agregar_arriendo (request):
    return render(request, 'arriendo/agregar_arriendo.html')


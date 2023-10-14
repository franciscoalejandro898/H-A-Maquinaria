from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    
    path('', views.index, name='home'),
    path("login/", views.login, name="login"),
    
    #URL MAQUINARIAS
    path("maquinaria/", views.maquinaria, name="maquinaria"),
    path("agregar_maquinaria/", views.agregar_maquinaria, name='agregar_maquinaria'),
   
    #URL CLIENTES
    path("clientes/", views.clientes, name="clientes"),
    path("agregar_cliente/", views.agregar_cliente, name="agregar_cliente"),
    path("editar_cliente/", views.editar_cliente, name="editar_cliente"),
    path("eliminar_cliente/", views.eliminar_cliente, name="eliminar_cliente"),
    
    #URL ARRIENDO
    path("arriendo/", views.arriendo, name="arriendo"),
    path("agregar_arriendo/", views.agregar_arriendo, name="agregar_arriendo"),    
]
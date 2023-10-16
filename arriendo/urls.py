from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    
    path('', views.index, name='home'),
    path("login/", views.login, name="login"),
    
    #URL MAQUINARIAS
    path("maquinaria/", views.maquinaria, name="maquinaria"),
    path("agregar_maquinaria/", views.agregar_maquinaria, name='agregar_maquinaria'),
    path("eliminar_maquinaria/<int:id_m>", views.eliminar_maquinaria, name='eliminar_maquinaria'),
    path("editar_maquinaria/<int:id_m>", views.editar_maquinaria, name='editar_maquinaria'),
    
   
    #URL CLIENTES
    path("clientes/", views.clientes, name="clientes"),
    path("agregar_cliente/", views.agregar_cliente, name="agregar_cliente"),
    path("editar_cliente/<int:id_cliente>", views.editar_cliente, name="editar_cliente"),
    path('eliminar_cliente/<int:id_cliente>', views.eliminar_cliente, name="eliminar_cliente"),
    
    #URL ARRIENDO
    path("arriendo/", views.arriendo, name="arriendo"),
    path("agregar_arriendo/", views.agregar_arriendo, name="agregar_arriendo"),   
    path("eliminar_arriendo/<int:id_arriendo>", views.eliminar_arriendo, name="eliminar_arriendo"),  
    path("editar_arriendo/<int:id_arriendo>", views.editar_arriendo, name="editar_arriendo"),    
]
from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', views.index, name='home'),
    #URL LOGIN / LOGOUT
    path('login/', LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
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
    
    #URL GRAFICOS
    path('grafico-arriendos/', views.grafico_arriendos, name='grafico_arriendos'),
    path('grafico-arriendos3/', views.duracion_promedio_por_categoria, name='grafico1'),
    path('grafico-arriendos1/', views.chart_data2, name='grafico2'),
    path('grafico-arriendos3/', views.chart_data3, name='grafico3'),
    path('grafico-arriendos1/', views.chart_data, name='grafico4'),
    
    
    
    path('crearpdf/', views.capture_and_create_pdf, name='descargapdf'),
    
    

    #path('grafico-arriendo/', views.arriendos_chart, name='grafico_arriendo'),
    
    
]

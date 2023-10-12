from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path("login/", views.login, name="login"),
    path("maquinaria/", views.maquinaria, name="maquinaria"),
    path("agregar_maquinaria/", views.agregar_maquinaria, name='agregar_maquinaria'),
    path("clientes/", views.clientes, name="clientes"),
    path("agregar_cliente/", views.agregar_cliente, name="agregar_cliente"),
    path("arriendo/", views.arriendo, name="arriendo"),
    path("agregar_arriendo/", views.agregar_arriendo, name="agregar_arriendo"),    
]
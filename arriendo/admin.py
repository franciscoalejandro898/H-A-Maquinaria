from django.contrib import admin
from .models import *


# configuracion de django admin

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id_cat', 'nombre_cat')
    search_fields = ['nombre_cat']
    
    
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('id_bodega', 'nombre_bod')
    search_fields = ['nombre_bod']
    
    
    
class MaquinariaAdmin(admin.ModelAdmin):
    list_display = ('id_m','sku', 'nombre_m', 'categoria_m', 'bodega_m', 'valor_dia')
    
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'rut_empresa', 'razon_social', 'direccion_empresa', 'nombre_representante', 'apellido_representante', 'telefono', 'correo_empresa')
    
    
class ArriendosAdmin(admin.ModelAdmin):
 list_display = ('id_arriendo', 'maquina_arriendo', 'cliente_arriendo', 'bodega_arriendo', 'fecha_inicio', 'fecha_entrega', 'dias_arriendo', 'costo_total')    
class EstadoMaquinariaAdmin(admin.ModelAdmin):
    list_display = ('id_estado', 'nombre_est_maquina', 'estado')
    

admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Bodegas,BodegaAdmin)
admin.site.register(Maquinaria,MaquinariaAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Arriendos,ArriendosAdmin)
#admin.site.register(EstadoMaquinaria,EstadoMaquinariaAdmin)
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

    #Tabla Categorias
class Categorias(models.Model):
   id_cat = models.AutoField('Id Categoria',primary_key=True)
   nombre_cat = models.CharField('Tipo de Categoria',max_length=20)
   
   def categorias(self):
       return "{}".format(self.nombre_cat)
   
   def __str__(self):
       return self.categorias()
   
    #Tabla Bodega  
class Bodegas(models.Model):
    id_bodega = models.AutoField('Id Bodega', primary_key=True)
    nombre_bod = models.CharField('Nombre Bodega', max_length=30)
    
    def bodegas(self):
       return "{}".format(self.nombre_bod)
    
    def __str__(self):
       return self.bodegas()

    #Tabla Maquinaria

class Maquinaria(models.Model):
    id_m = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=20)
    nombre_m = models.CharField(max_length=20, verbose_name="Nombre Maquinaria")
    categoria_m = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, verbose_name="Categorias")
    bodega_m = models.ForeignKey(Bodegas, on_delete=models.SET_NULL, null=True)

    def maquinaria(self):
        return "{}".format(self.nombre_m)
    
    def estado(self):
        return "Disponible"
    
    def __str__(self):
        return self.maquinaria()

   
    #Tabla Cliente
class Cliente(models.Model):
   id_cliente = models.AutoField(primary_key=True)
   nombre = models.CharField( max_length=20)
   apellido = models.CharField( max_length=20)
   rut = models.CharField(max_length=40)
   telefono = models.CharField( max_length=20)
   
   def cliente(self):
       return "{}".format(self.nombre)
  
   
   def __str__(self):
       return self.cliente()
   
    #Tabla Arriendos 
class Arriendos(models.Model): 
    id_arriendo = models.AutoField(primary_key=True, blank=False)
    maquina_arriendo = models.ForeignKey(Maquinaria, on_delete=models.SET_NULL,null=True, blank=False)
    cliente_arriendo = models.ForeignKey(Cliente, on_delete=models.SET_NULL,null=True, blank=False)
    bodega_arriendo = models.ForeignKey(Bodegas, on_delete=models.SET_NULL,null=True, blank=False) 
    fecha_arriendo = models.DateField(null=False, blank=False)
    
    def arriendo(self):
       return "{} {} {} {} {}".format(self.id_arriendo,self.maquina_arriendo, self.cliente_arriendo, self.bodega_arriendo,self.fecha_arriendo)
    
    def __str__(self):
       return self.arriendo()
   
@receiver(post_save, sender=Arriendos)
def actualizar_estado_maquinaria(sender, instance, **kwargs):
    # Verifica si la maquinaria asociada al arriendo está en la instancia
   if instance.maquina_arriendo:
      instance.maquina_arriendo.estado = "No Disponible"
      instance.maquina_arriendo.save()
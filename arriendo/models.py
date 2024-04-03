from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
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
    sku = models.IntegerField(unique=True)
    nombre_m = models.CharField(max_length=20, verbose_name="Nombre Maquinaria")
    categoria_m = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, verbose_name="Categorias")
    bodega_m = models.ForeignKey(Bodegas, on_delete=models.SET_NULL, null=True)
    valor_dia = models.DecimalField(max_digits=10, decimal_places=0)

    def maquinaria(self):
        return "{}".format(self.nombre_m)
    
    def estado(self):
        return "Disponible"
    
    def __str__(self):
        return self.maquinaria()

   
    #Tabla Cliente
class Cliente(models.Model):
   id_cliente = models.AutoField(primary_key=True)
   rut_empresa = models.IntegerField(unique=True)
   razon_social = models.CharField( max_length=30)
   direccion_empresa = models.CharField( max_length=30)
   nombre_representante = models.CharField( max_length=30)
   apellido_representante = models.CharField( max_length=20)
   telefono = models.IntegerField(unique=True)
   correo_empresa = models.EmailField(default="")
   
   def cliente(self):
       return "{}".format(self.razon_social)
  
   
   def __str__(self):
       return self.cliente()
   
    #Tabla Arriendos 
class Arriendos(models.Model):
    id_arriendo = models.AutoField(primary_key=True, blank=False)
    maquina_arriendo = models.ForeignKey(Maquinaria, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Maquinaria")
    cliente_arriendo = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Cliente")
    bodega_arriendo = models.ForeignKey(Bodegas, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Bodega")
    fecha_inicio = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)
    dias_arriendo = models.IntegerField(blank=True, null=True, verbose_name="Cantidad de días")
    costo_total = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    
    def __str__(self):
        # Formatea el costo_total como pesos chilenos con símbolo "$" y punto como separador de miles
        costo_total_formateado = f"${self.costo_total:,.0f}".replace(",", ".")
        return f"ID: {self.id_arriendo} - Maquinaria: {self.maquina_arriendo.nombre_m} - Cliente: {self.cliente_arriendo.razon_social} - Costo Total: {costo_total_formateado}"
    
    def save(self, *args, **kwargs):
        # Calcular la duración del arriendo y el costo total
        if self.fecha_entrega and self.fecha_inicio:
            self.dias_arriendo = (self.fecha_entrega - self.fecha_inicio).days
            self.costo_total = self.dias_arriendo * self.maquina_arriendo.valor_dia
        super(Arriendos, self).save(*args, **kwargs)
    
   
#@receiver(post_save, sender=Arriendos)
#def actualizar_estado_maquinaria(sender, instance, **kwargs):
    # Verifica si la maquinaria asociada al arriendo está en la instancia
   #if instance.maquina_arriendo:
      #instance.maquina_arriendo.estado = "No Disponible"
      #instance.maquina_arriendo.save()
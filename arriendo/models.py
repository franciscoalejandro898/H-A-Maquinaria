from django.db import models

# definicion de los modelos


from django.db import models

# Create your models here.
#Tabla Categorias
class Categorias(models.Model):
   id_cat = models.AutoField('Id Categoria',primary_key=True)
   nombre_cat = models.CharField('Tipo de Categoria',max_length=20)
   
   def categorias(self):
       return "{} {}".format(self.id_cat,self.nombre_cat)
   
   def __str__(self):
       return self.categorias()
   
    #Tabla Bodega  
class Bodegas(models.Model):
    id_bodega = models.AutoField('Id Bodega', primary_key=True)
    nombre_bod = models.CharField('Nombre Bodega', max_length=30)
    
    def bodegas(self):
       return "{} {}".format(self.id_bodega,self.nombre_bod)
    
    def __str__(self):
       return self.bodegas()

    #Tabla Maquinaria

class Maquinaria(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('no_disponible', 'No Disponible'),
    ]
    
    id_m = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=20)
    nombre_m = models.CharField(max_length=20)
    categoria_m = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    bodega_m = models.ForeignKey(Bodegas, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')

   
    def maquinaria(self):
       return "{} {} {} {} {}".format(self.id_m,self.nombre_m, self.categoria_m, self.bodega_m, self.estado)
   
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
       return "{} {} {} {} {}".format(self.id_cliente,self.nombre,self.apellido, self.rut,self.telefono)
  
   
   def __str__(self):
       return self.cliente()
   
    #Tabla Arriendos 
class Arriendos(models.Model): 
    id_arriendo = models.AutoField(primary_key=True)
    maquina_arriendo = models.ForeignKey(Maquinaria, on_delete=models.SET_NULL,null=True)
    cliente_arriendo = models.ForeignKey(Cliente, on_delete=models.SET_NULL,null=True)
    bodega_arriendo = models.ForeignKey(Bodegas, on_delete=models.SET_NULL,null=True)
    fecha_arriendo = models.DateField(null=False, blank=False)
    
    def arriendo(self):
       return "{} {} {} {} {}".format(self.id_arriendo,self.maquina_arriendo, self.cliente_arriendo, self.bodega_arriendo,self.fecha_arriendo)
    
    def __str__(self):
       return self.arriendo()
   
   #Tabla EstadoMaquinaria
class EstadoMaquinaria(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_est_maquina = models.ForeignKey(Maquinaria,on_delete=models.SET_NULL,null=True)
    l_estado = (('Y', 'Disponible'), ('N', 'No Disponible'))
    estado = models.CharField(max_length=1,choices=l_estado,default='Y')
    
    
    def estado_maquinaria(self):
       return "{} {} {}".format(self.id_estado,self.nombre_est_maquina,self.estado)
    
    def __str__(self):
       return self.estado_maquinaria()
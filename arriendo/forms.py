from django import forms
from .models import *


#Formulario para agregar clientes
class ClienteForm(forms.ModelForm): 
    class Meta:
        model = Cliente
        fields = '__all__'
        
#Formulario para agregar maquinarias
class MaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        fields = '__all__'
        
#Formulario para agregar arriendos

class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendos
        fields = '__all__'
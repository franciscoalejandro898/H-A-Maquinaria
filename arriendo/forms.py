from django import forms
from .models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput 


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
        widgets = {
            'fecha_inicio': DatePickerInput(),  # Aplicar DatePickerInput al campo fecha_inicio
            'fecha_entrega': DatePickerInput(),  # Aplicar DatePickerInput al campo fecha_entrega
        }
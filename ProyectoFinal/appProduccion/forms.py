
from django import forms

class FormularioCliente(forms.Form):
    razonSocial = forms.CharField()
    cuit = forms.CharField()
    direccion = forms.CharField()
    provincia = forms.CharField()
    codigoPostal = forms.IntegerField()

class FormularioFabrica(forms.Form):
    razonSocial = forms.CharField()
    cuit = forms.CharField()
    direccion = forms.CharField()
    provincia = forms.CharField()
    codigoPostal = forms.IntegerField()

class FormularioHilado(forms.Form):
    Partida = forms.IntegerField()
    Articulo = forms.CharField()    
    Codigo_Color = forms.CharField()
    Kg = forms.IntegerField() 
    Conos_Totales = forms.IntegerField()
    Fecha_de_teñido = forms.CharField() 
    Estado =  forms.CharField() 
    Cliente_1 = forms.CharField() 
    Cliente_2 = forms.CharField()
    Cliente_3 = forms.CharField()
    Cliente_4 = forms.CharField()
    Cliente_5 = forms.CharField()
    
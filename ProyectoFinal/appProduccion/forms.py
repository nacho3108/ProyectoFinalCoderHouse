from django import forms

class FormularioCliente(forms.Form):
    razonSocial = forms.CharField()
    cuit = forms.CharField()
    direccion = forms.CharField()
    provincia = forms.CharField()
    codigoPostal = forms.IntegerField()
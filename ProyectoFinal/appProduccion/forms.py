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
    codigoColor = forms.IntegerField()
    partida = forms.IntegerField()
    ordenPedido = forms.IntegerField()
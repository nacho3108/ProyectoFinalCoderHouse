
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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


class UserEditForm(UserChangeForm): #Usuario eredado de UserChangeForm pero con menos campos, solo los que queremos
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    #Voy a dejar que cambie tambien la contraseña
    password1 = forms.CharField(label= "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la contraseña", widget = forms.PasswordInput)
    class Meta: #Meta es para decirle a que modelo está asociado

        model = User
        fields = ['email', 'first_name', 'last_name']
    
    def clean_password2(self):#para agregar validación dentro del formulario, en este caso sobre password2 pero podria ser pass1
        password2 = self.cleaned_data["password2"]
        if (password2!=self.cleaned_data["password1"]):
            raise forms.ValidationError("Las contraseñas no coinciden") #lanzo error 
        return password2 #no hace falta poner un else porque el raise corta
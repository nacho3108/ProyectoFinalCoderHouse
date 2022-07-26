from django.http import HttpResponse
from django.shortcuts import render

from appProduccion.models import Cliente, Fabrica
from appProduccion.forms import FormularioCliente, FormularioFabrica

# Create your views here.
def inicio(request):
    return render(request,"appProduccion/inicio.html")

def fabricas(request):
    return render(request,"appProduccion/fabricas.html")

def clientes(request):
    return render(request,"appProduccion/clientes.html")

def hilados(request):
    return render(request,"appProduccion/hilados.html")

def formularioCliente(request):
    if request.method == 'POST':

        miFormulario = FormularioCliente(request.POST) #Aqui nos llega toda la info del html

        print(miFormulario)

        if miFormulario.is_valid: #si paso la validación de django
                informacion = miFormulario.cleaned_data
 
                cliente = Cliente (razonSocial=informacion['razonSocial'],cuit=informacion['cuit'],direccion=informacion['direccion'],provincia=informacion['provincia'],codigoPostal=informacion['codigoPostal'])

                cliente.save()

                return render(request, "appProduccion/inicio.html")
    
    else:
         miFormulario = FormularioCliente() #Formulario Vacio para construir el html


    return render(request,"appProduccion/formularioCliente.html",{"miFormulario":miFormulario})


def formularioFabrica(request):
    if request.method == 'POST':

        miFormulario = FormularioFabrica(request.POST) #Aqui nos llega toda la info del html

        print(miFormulario)

        if miFormulario.is_valid: #si paso la validación de django
                informacion = miFormulario.cleaned_data
 
                fabrica = Fabrica (razonSocial=informacion['razonSocial'],cuit=informacion['cuit'],direccion=informacion['direccion'],provincia=informacion['provincia'],codigoPostal=informacion['codigoPostal'])

                fabrica.save()

                return render(request, "appProduccion/inicio.html")
    
    else:
         miFormulario = FormularioFabrica() #Formulario Vacio para construir el html


    return render(request,"appProduccion/formularioFabrica.html",{"miFormulario":miFormulario})


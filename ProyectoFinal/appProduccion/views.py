
from django.http import HttpResponse
from django.shortcuts import render


from appProduccion.models import Cliente, Fabrica, Hilado
from appProduccion.forms import FormularioCliente, FormularioFabrica, FormularioHilado

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

def formularioHilado(request):
    if request.method == 'POST':

        miFormulario = FormularioHilado(request.POST) #Aqui nos llega toda la info del html

        print(miFormulario)

        if miFormulario.is_valid: #si paso la validación de django
                informacion = miFormulario.cleaned_data
 
                hilado = Hilado (codigoColor=informacion['codigoColor'],partida=informacion['partida'],ordenPedido=informacion['ordenPedido'])

                hilado.save()

                return render(request, "appProduccion/inicio.html")
    
    else:
         miFormulario = FormularioHilado() #Formulario Vacio para construir el html


    return render(request,"appProduccion/formularioHilado.html",{"miFormulario":miFormulario})

def busquedaCliente(request):
    return render(request, "appProduccion/busquedaCliente.html")

#def buscar(request):
#   respuesta = f"Busacando al cliente: {request.GET['cliente']}"

 #   return HttpResponse(respuesta)

def buscar(request):
 

    if request.GET["cliente"]:

        cliente = request.GET["cliente"]

        clientes = Cliente.objects.filter(razonSocial__icontains=cliente)

        return render(request, "appProduccion/resultadoBusqueda.html", {"clientes": clientes, "cliente": cliente})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def __str__(self):
    return f"Razón Social: {self.razonSocial} - CUIT: {self.cuit} - Direccion: {self.direccion} - Provincia: {self.provincia} - Código Postal: {self.codigoPostal}"


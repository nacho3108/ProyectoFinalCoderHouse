
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

def buscarCliente(request):
 

    if request.GET["cliente"]:

        cliente = request.GET["cliente"]

        clientes = Cliente.objects.filter(razonSocial__icontains=cliente)

        return render(request, "appProduccion/buscarCliente.html", {"clientes": clientes, "cliente": cliente})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def leerFabricas(request):
    fabricas = Fabrica.objects.all() #traigo todas las fábricas

    contexto = {"fabricas":fabricas}

    return render(request, "appProduccion/leerFabricas.html",contexto)

def leerClientes(request):
    clientes = Cliente.objects.all() 

    contexto = {"clientes":clientes}

    return render(request, "appProduccion/leerClientes.html",contexto)

def leerHilados(request):
    hilados = Hilado.objects.all() 

    contexto = {"hilados":hilados}

    return render(request, "appProduccion/leerHilados.html",contexto)

def eliminoFabrica(request, id):
    
    if request.method == 'POST':
        
        fabrica = Fabrica.objects.get(id=id) #id unico

        fabrica.delete()

        #Vuelvo al menu y ya se borro fabrica

        fabricas = Fabrica.objects.all() #traigo todas las fabricas

        contexto = {"fabricas":fabricas}

        return render(request, "appProduccion/leerFabricas.html",contexto)

def editarFabrica(request, id):
    
    fabrica = Fabrica.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = FormularioFabrica(request.POST) #Aqui nos llega toda la info del html

        print(miFormulario)

        if miFormulario.is_valid: #si paso la validación de django
                informacion = miFormulario.cleaned_data
 
                fabrica.razonSocial = informacion["razonSocial"]
                fabrica.cuit = informacion["cuit"]
                fabrica.direccion = informacion["direccion"]
                fabrica.provincia = informacion["provincia"]
                fabrica.codigoPostal = informacion["codigoPostal"]

                fabrica.save()

                return render(request, "appProduccion/inicio.html")
    
    else:

        miFormulario = FormularioFabrica(initial={
            "razonSocial" : fabrica.razonSocial,
            "cuit": fabrica.cuit,
            "direccion": fabrica.direccion,
            "provincia": fabrica.provincia,
            "codigoPostal": fabrica.codigoPostal,
        }) #como vamos a editar no puede ser vacio


    return render(request,"appProduccion/editarFabrica.html",{"miFormulario":miFormulario, "id":fabrica.id}) #necesito no perder el id

def busquedaFabrica(request):
    return render(request, "appProduccion/busquedaFabrica.html")


def buscarFabrica(request):
 

    if request.GET["fabrica"]:

        fabrica = request.GET["fabrica"]

        fabricas = Fabrica.objects.filter(razonSocial__icontains=fabrica)

        return render(request, "appProduccion/buscarFabrica.html", {"fabricas": fabricas, "fabrica": fabrica})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)
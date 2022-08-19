
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AvatarFormulario, UserEditForm


from appProduccion.models import Avatar, Cliente, Fabrica, Hilado
from appProduccion.forms import FormularioCliente, FormularioFabrica, FormularioHilado
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clase (permisos de usuario)
from django.contrib.auth.decorators import login_required #decorador para visatas basadas en funciones (permisos de usuarios)
from django.contrib.admin.views.decorators import staff_member_required #decorador para no permitir acceso a usuarios menor nivel

# Create your views here.

def inicio(request):
    try:
        avatar = Avatar.objects.get(user = request.user.id)
        return render(request,"appProduccion/inicio.html",{"url":avatar.imagen.url})

    except:
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
 
                hilado = Hilado (partida=informacion['Partida'],articulo=informacion['Articulo'],codigoColor=informacion['Codigo_Color'],
                kg=informacion['Kg'],cantidadConos=informacion['Conos_Totales'],fechaTenido=informacion['Fecha_de_teñido'],estado=informacion['Estado'],
                clienteTenido1=informacion['Cliente_1'],clienteTenido2=informacion['Cliente_2'],clienteTenido3=informacion['Cliente_3'],clienteTenido4=informacion['Cliente_4'],
                clienteTenido5=informacion['Cliente_5'])



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


@login_required
def leerFabricas(request):


    fabricas = Fabrica.objects.all() #traigo todas las fábricas

    contexto = {"fabricas":fabricas}

    
    return render(request, "appProduccion/leerFabricas.html",contexto)

@login_required
def leerClientes(request):
    clientes = Cliente.objects.all() 

    contexto = {"clientes":clientes}

    return render(request, "appProduccion/leerClientes.html",contexto)

@login_required
def leerHilados(request):
    hilados = Hilado.objects.all() 

    contexto = {"hilados":hilados}

    return render(request, "appProduccion/leerHilados.html",contexto)
@login_required
def eliminoFabrica(request, id):
    
    if request.method == 'POST':
        
        fabrica = Fabrica.objects.get(id=id) #id unico

        fabrica.delete()

        #Vuelvo al menu y ya se borro fabrica

        fabricas = Fabrica.objects.all() #traigo todas las fabricas

        contexto = {"fabricas":fabricas}

        return render(request, "appProduccion/leerFabricas.html",contexto)
@login_required
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
@login_required
def busquedaFabrica(request):
    return render(request, "appProduccion/busquedaFabrica.html")

@login_required
def buscarFabrica(request):
 

    if request.GET["fabrica"]:

        fabrica = request.GET["fabrica"]

        fabricas = Fabrica.objects.filter(razonSocial__icontains=fabrica)

        return render(request, "appProduccion/buscarFabrica.html", {"fabricas": fabricas, "fabrica": fabrica})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def busquedaHilado(request):
    return render(request, "appProduccion/busquedaHilado.html")

@login_required
def buscarHilado(request):
 

    if request.GET["hilado"]:

        hilado = request.GET["hilado"]

        hilados = Hilado.objects.filter(codigoColor=hilado)

        return render(request, "appProduccion/buscarHilado.html", {"hilados": hilados, "hilado": hilado})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

class ClienteList(ListView):
    
    model = Cliente
    template_name = 'appProduccion/cliente_list.html'
    context_object_name = 'clientes' #recibe como contexto la lista de clientes 

class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'appProduccion/cliente_detail.html'
    context_object_name = 'cliente' #recibe como contexto el cliente para hacer el detalle


class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'appProduccion/cliente_create.html'
    fields = ["razonSocial", "cuit", "direccion", "provincia","codigoPostal"]#campos que queremos que se renderizen para generar el registro
    success_url = '/appProduccion/'#template de exito
class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'appProduccion/cliente_update.html'
    fields = ('__all__') # es otra forma de agregar todos los campos que hay
    success_url = '/appProduccion/'#template de exito
class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'appProduccion/cliente_delete.html'
    success_url = '/appProduccion/'#template de exito


#-------------------------------------CRUD---Hilado


class HiladoList(LoginRequiredMixin, ListView):
    model = Hilado
    template_name = 'appProduccion/hilado_list.html'
    context_object_name = 'hilados' #recibe como contexto la lista de hilados 

class HiladoDetail(DetailView):
    model = Hilado
    template_name = 'appProduccion/hilado_detail.html'
    context_object_name = 'hilado' #recibe como contexto el hilado para hacer el detalle


class HiladoCreate(CreateView):
    model = Hilado
    template_name = 'appProduccion/hilado_create.html'
    fields = ('__all__') #campos que queremos que se renderizen para generar el registro
    success_url = '/appProduccion/listaHilados/'#template de exito

class HiladoUpdate(UpdateView):
    model = Hilado
    template_name = 'appProduccion/hilado_update.html'
    fields = ('__all__') # es otra forma de agregar todos los campos que hay
    success_url = '/appProduccion/listaHilados/'#template de exito
class HiladoDelete(DeleteView):
    model = Hilado
    template_name = 'appProduccion/hilado_delete.html'
    success_url = '/appProduccion/listaHilados/'#template de exito

#---------------LOGIN-----------------------

def login_request(request):

    if request.method == "POST":

        miFormulario = AuthenticationForm(request, data = request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario = data['username']
            psw = data['password']

            user = authenticate(username = usuario, password = psw) 

            if user:
                login(request,user)
                
                return render(request, 'appProduccion/inicio.html', {"mensaje": f'Bienvenido {usuario}'})
            else:
                return render(request, 'appProduccion/inicio.html', {"mensaje": "Error, datos incorrectos"})
    
        

        return render(request, 'appProduccion/inicio.html', {"mensaje": "Error, Formulario invalido"})
    
    else:
        miFormulario = AuthenticationForm()

    return render(request, "appProduccion/login.html", {'miFormulario':miFormulario})

    #----------------REGISTRO DE NUEVOS USUARIOS

def register(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
                
            username = form.cleaned_data["username"]

            form.save()

            
            return render(request, 'appProduccion/inicio.html', {"mensaje": f"Usuario {username} creado"} )
    else:

        form = UserCreationForm()
        
    return render(request, "appProduccion/registro.html", {'miFormulario':form})


#---------------Edicion usuario-----------------------
@login_required #si no esta logueado no puede editar
def editarPerfil(request):

    usuario = request.user


    if request.method == "POST":

        miFormulario = UserEditForm(request.POST, instance = request.user)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']

            usuario.save()
        
        
            return render(request, 'appProduccion/inicio.html', {"mensaje": "Datos actualozados con exito"})
    
    else:
        miFormulario = UserEditForm(instance = request.user)#datos cargados de perfil existente

    return render(request, "appProduccion/editarPerfil.html", {'miFormulario':miFormulario})


#-------------Agrega AVATAR--------
def agregarAvatar(request):
    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)  #las imagenes viene en el request.FILES

        print(miFormulario)

        if miFormulario.is_valid: #si paso la validación de django

                data = miFormulario.cleaned_data
 
                
                avatar = Avatar(user=request.user, imagen=data['imagen'])

                avatar.save()

                return render(request, "appProduccion/inicio.html",{"mensaje": "Avatar cargado correctamente"})
    
    else:
         miFormulario = AvatarFormulario() #Formulario Vacio para construir el html


    return render(request,"appProduccion/agregarAvatar.html",{"miFormulario":miFormulario})

from django.urls import path


from appProduccion.views import (
    fabricas, clientes, inicio, formularioCliente, formularioFabrica, busquedaFabrica, buscarFabrica, busquedaHilado, buscarHilado,
    formularioHilado, busquedaCliente, buscarCliente, leerFabricas, leerClientes, eliminoFabrica, editarFabrica, 
    ClienteList, ClienteDetail, ClienteCreate, ClienteUpdate, ClienteDelete, HiladoCreate, HiladoDelete, HiladoDetail, HiladoList, HiladoUpdate,
    login_request, register
    )



urlpatterns = [
    path('', inicio, name="Inicio"),
    path('fabricas/', fabricas, name="Fabrica"),
    path('clientes/', clientes, name="Clientes"),
   
    path('formularioCliente/', formularioCliente, name="FormularioClientes"),
    path('formularioFabrica/', formularioFabrica, name="FormularioFabrica"),
    path('formularioHilado/', formularioHilado, name="FormularioHilado"),
    path('busquedaCliente/', busquedaCliente, name="BusquedaCliente"),
    path('buscarCliente/', buscarCliente, name="BuscarCliente"),
    path('leerFabricas/', leerFabricas, name="LeerFabricas"),
    path('leerClientes/', leerClientes, name="LeerClientes"),
    
    path('eliminoFabrica/<int:id>', eliminoFabrica, name="EliminoFabrica"),
    path('editarFabrica/<int:id>', editarFabrica, name="EditarFabrica"),
    path('busquedaFabrica/', busquedaFabrica, name="BusquedaFabrica"),
    path('buscarFabrica/', buscarFabrica, name="BuscarFabrica"),
    
    path('buscarHilado/', buscarHilado, name="BuscarHilado"),
    path('listaClientes/', ClienteList.as_view(), name="ListaClientes"),
    path('detalleCliente/<int:pk>', ClienteDetail.as_view(), name="DetalleCliente"),
    path('creaCliente/', ClienteCreate.as_view(), name="CreaCliente"),
    path('actualizaCliente/<int:pk>', ClienteUpdate.as_view(), name="ActualizaCliente"),
    path('eliminaCliente/<int:pk>', ClienteDelete.as_view(), name="EliminaCliente"),
    
    
    path('listaHilados/', HiladoList.as_view(), name="ListaHilados"),
    path('detalleHilado/<int:pk>', HiladoDetail.as_view(), name="DetalleHilado"),
    path('creaHilado/', HiladoCreate.as_view(), name="CreaHilado"),
    path('actualizaHilado/<int:pk>', HiladoUpdate.as_view(), name="ActualizaHilado"),
    path('eliminaHilado/<int:pk>', HiladoDelete.as_view(), name="EliminaHilado"),

    path('buscarHilado/', buscarHilado, name="BuscarHilado"),
    path('busquedaHilado/', busquedaHilado, name="BusquedaHilado"),

    path('login/', login_request, name="Login"),
    path('registrar/', register, name="Registrar"),



]
from django.urls import path

from appProduccion.views import (
    fabricas, clientes, hilados, inicio, formularioCliente, formularioFabrica, busquedaFabrica, buscarFabrica, busquedaHilado, buscarHilado,
    formularioHilado, busquedaCliente, buscarCliente, leerFabricas, leerClientes, leerHilados, eliminoFabrica, editarFabrica, 
    ClienteList, ClienteDetail, ClienteCreate, ClienteUpdate, ClienteDelete
    )


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('fabricas/', fabricas, name="Fabrica"),
    path('clientes/', clientes, name="Clientes"),
    path('hilados/', hilados, name="Hilados"),
    path('formularioCliente/', formularioCliente, name="FormularioClientes"),
    path('formularioFabrica/', formularioFabrica, name="FormularioFabrica"),
    path('formularioHilado/', formularioHilado, name="FormularioHilado"),
    path('busquedaCliente/', busquedaCliente, name="BusquedaCliente"),
    path('buscarCliente/', buscarCliente, name="BuscarCliente"),
    path('leerFabricas/', leerFabricas, name="LeerFabricas"),
    path('leerClientes/', leerClientes, name="LeerClientes"),
    path('leerHilados/', leerHilados, name="LeerHilados"),
    path('eliminoFabrica/<int:id>', eliminoFabrica, name="EliminoFabrica"),
    path('editarFabrica/<int:id>', editarFabrica, name="EditarFabrica"),
    path('busquedaFabrica/', busquedaFabrica, name="BusquedaFabrica"),
    path('buscarFabrica/', buscarFabrica, name="BuscarFabrica"),
    path('busquedaHilado/', busquedaHilado, name="BusquedaHilado"),
    path('buscarHilado/', buscarHilado, name="BuscarHilado"),
    path('listaClientes/', ClienteList.as_view(), name="ListaClientes"),
    path('detalleCliente/<int:pk>', ClienteDetail.as_view(), name="DetalleCliente"),
    path('creaCliente/', ClienteCreate.as_view(), name="CreaCliente"),
    path('actualizaCliente/<int:pk>', ClienteUpdate.as_view(), name="ActualizaCliente"),
    path('eliminaCliente/<int:pk>', ClienteDelete.as_view(), name="EliminaCliente"),

]
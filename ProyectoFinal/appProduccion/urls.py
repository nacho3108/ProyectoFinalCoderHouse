from django.urls import path

from appProduccion.views import fabricas, clientes, hilados, inicio, formularioCliente, formularioFabrica, formularioHilado, busquedaCliente, buscar


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('fabricas/', fabricas, name="Fabrica"),
    path('clientes/', clientes, name="Clientes"),
    path('hilados/', hilados, name="Hilados"),
    path('formularioCliente/', formularioCliente, name="FormularioClientes"),
    path('formularioFabrica/', formularioFabrica, name="FormularioFabrica"),
    path('formularioHilado/', formularioHilado, name="FormularioHilado"),
    path('busquedaCliente/', busquedaCliente, name="busquedaCliente"),
    path('buscar/', buscar, name="Buscar"),
]
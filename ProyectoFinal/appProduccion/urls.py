from django.urls import path
from appProduccion.views import fabricas, clientes, hilados, inicio


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('fabricas/', fabricas, name="Fabrica"),
    path('clientes/', clientes, name="Clientes"),
    path('hilados/', hilados, name="Hilados"),
]
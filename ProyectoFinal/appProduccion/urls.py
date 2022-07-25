from django.urls import path
from appProduccion import views
from appProduccion.views import fabricas, clientes, hilados, inicio


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('fabricas/', views.fabricas, name="Fabrica"),
    path('clientes/', views.clientes, name="Clientes"),
    path('hilados/', views.hilados, name="Hilados"),
]
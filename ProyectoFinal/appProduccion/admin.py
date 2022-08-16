from django.contrib import admin

from appProduccion.models import Avatar, Cliente, Fabrica, Hilado

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Fabrica)
admin.site.register(Hilado)
admin.site.register(Avatar)

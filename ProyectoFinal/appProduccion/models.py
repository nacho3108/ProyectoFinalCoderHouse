from django.db import models

# Create your models here.
class Fabrica(models.Model):

    razonSocial = models.CharField(max_length=50)
    cuit = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    
class Cliente(models.Model):

    razonSocial = models.CharField(max_length=50)
    cuit = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()

class Hilado(models.Model):

    codigoColor = models.IntegerField()
    partida = models.IntegerField()
    ordenPedido = models.IntegerField()


from django.db import models

# Create your models here.
class Fabrica(models.Model):

    razonSocial = models.CharField(max_length=50)
    cuit = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()

    def __str__(self):
        return f"Razón Social: {self.razonSocial} - CUIT: {self.cuit} - Direccion: {self.direccion} - Provincia: {self.provincia} - Código Postal: {self.codigoPostal}"
    
class Cliente(models.Model):

    razonSocial = models.CharField(max_length=50)
    cuit = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()

    def __str__(self):
        return f"Razón Social: {self.razonSocial} - CUIT: {self.cuit} - Direccion: {self.direccion} - Provincia: {self.provincia} - Código Postal: {self.codigoPostal}"


class Hilado(models.Model):

    codigoColor = models.IntegerField()
    partida = models.IntegerField()
    ordenPedido = models.IntegerField()

    def __str__(self):
        return f"Código color: {self.codigoColor} - Partida: {self.partida} - Orden de Pedido nº: {self.ordenPedido}"



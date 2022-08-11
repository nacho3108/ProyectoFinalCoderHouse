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

    partida = models.IntegerField()
    articulo =  models.CharField(max_length=30)    #el artículo puede ser Gong, Milan, etc
    codigoColor = models.IntegerField() #el código de color es el color con que se tiñe y puede ser el mismo para distintos artículos
    kg = models.IntegerField() 
    cantidadConos = models.IntegerField() 
    fechaTenido = models.DateField()
    estado =  models.CharField(max_length=20) #puede ser: (TINTORERIA/HUMEDO/SECO/DEVANADO/DEPOSITO)
    clienteTenido1 = models.CharField(max_length=50) #En algun momento tengo que vincular esto con clientes cargados
    clienteTenido2 = models.CharField(max_length=50)
    clienteTenido3 = models.CharField(max_length=50)
    clienteTenido4 = models.CharField(max_length=50)
    clienteTenido5 = models.CharField(max_length=50)
    
        
    
    def __str__(self):
        return f"Partida: {self.partida} - Artículo: {self.articulo} - Código Color: {self.codigoColor} - KG: {self.kg} - Conos: {self.cantidadConos} - Fecha Teñido: {self.fechaTenido} - Estado: {self.estado}- Cliente 1: {self.clienteTenido1} - Cliente 2: {self.clienteTenido2} - Cliente 3: {self.clienteTenido3} - Cliente 4: {self.clienteTenido4} - Cliente 5: {self.clienteTenido5} "



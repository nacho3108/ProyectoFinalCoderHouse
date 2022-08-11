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
    
    #Hasta acá se carga cuando se crea una partida nueva (se tiñó)
    #A continuación estos campos deben ser inicializados sin valor para darle valor a la hora de la entrega
    #Estimo que una partida de Hilado se le puede entregar como máximo a 10 clientes distintos
    #En algun lugar hay que hacer un control para que si de una partida de 144 conos se entregaron 100, no se le puedan entregar a otro cliente mas de 44 conos 
    clienteEntrega1 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega1 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega1 = models.IntegerField() 
    fechaEntrega1 = models.DateField()
    clienteEntrega2 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega2 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega2 = models.IntegerField() 
    fechaEntrega2 =models.DateField()
    clienteEntrega3 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega3 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega3 = models.IntegerField() 
    fechaEntrega3 =models.DateField()
    clienteEntrega4 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega4 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega4 = models.IntegerField() 
    fechaEntrega4 = models.DateField()
    clienteEntrega5 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega5 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega5 = models.IntegerField() 
    fechaEntrega5 = models.DateField()
    clienteEntrega6 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega6 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega6 = models.IntegerField() 
    fechaEntrega6 = models.DateField()
    clienteEntrega7 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega7 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega7 = models.IntegerField() 
    fechaEntrega7 = models.DateField()
    clienteEntrega8 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega8 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega8 = models.IntegerField() 
    fechaEntrega8 = models.DateField()
    clienteEntrega9 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega9 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega9 = models.IntegerField() 
    fechaEntrega9 = models.DateField()
    clienteEntrega10 = models.CharField(max_length=50) #puede ser cambiado el cliente a la hora de entrega, tener cuidado que hay que modificar la oden de pedido si eso pasa
    kgEntrega10 = models.IntegerField() #Cuando se crea una partida se estiman los kg, pero en producción hay desperdicios que se ven con los kg entregados
    conosEntrega10 = models.DateField()
    fechaEntrega10 = models.CharField(max_length=10)
    
    
    def __str__(self):
        return f"Partida: {self.partida} - Artículo: {self.articulo} - Código Color: {self.codigoColor} - KG: {self.kg} - Conos: {self.cantidadConos} - Fecha Teñido: {self.fechaTenido} - Estado: {self.estado}- Cliente 1: {self.clienteTenido1} - Cliente 2: {self.clienteTenido2} - Cliente 3: {self.clienteTenido3} - Cliente 4: {self.clienteTenido4} - Cliente 5: {self.clienteTenido5} - Cliente Entrega 1: {self.clienteEntrega1} - Kg: {self.kgEntrega1} - Conos: {self.conosEntrega1} - Fecha: {self.fechaEntrega1} - Cliente Entrega 2: {self.clienteEntrega2} - Kg: {self.kgEntrega2} - Conos: {self.conosEntrega2} - Fecha: {self.fechaEntrega2} - Cliente Entrega 3: {self.clienteEntrega3} - Kg: {self.kgEntrega3} - Conos: {self.conosEntrega3} - Fecha: {self.fechaEntrega3} - Cliente Entrega 4: {self.clienteEntrega4} - Kg: {self.kgEntrega4} - Conos: {self.conosEntrega4} - Fecha: {self.fechaEntrega4} - Cliente Entrega 5: {self.clienteEntrega5} - Kg: {self.kgEntrega5} - Conos: {self.conosEntrega5} - Fecha: {self.fechaEntrega5} - Cliente Entrega 6: {self.clienteEntrega6} - Kg: {self.kgEntrega6} - Conos: {self.conosEntrega6} - Fecha: {self.fechaEntrega6} - Cliente Entrega 7: {self.clienteEntrega7} - Kg: {self.kgEntrega7} - Conos: {self.conosEntrega7} - Fecha: {self.fechaEntrega7} - Cliente Entrega 8: {self.clienteEntrega8} - Kg: {self.kgEntrega8} - Conos: {self.conosEntrega8} - Fecha: {self.fechaEntrega8} - Cliente Entrega 9: {self.clienteEntrega9} - Kg: {self.kgEntrega9} - Conos: {self.conosEntrega9} - Fecha: {self.fechaEntrega9} - Cliente Entrega 10: {self.clienteEntrega10} - Kg: {self.kgEntrega10} - Conos: {self.conosEntrega10} - Fecha: {self.fechaEntrega10}  "



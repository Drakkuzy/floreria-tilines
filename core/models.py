from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from api.models import *



# Create your models here.

    

class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    oferta = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField()
    imagen = models.CharField(max_length=200)
    
    def __str__(self):
        return self.codigo+" - "+self.descripcion
    
    
class Venta(models.Model):
    
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, default="EN PREPARACION")
    total = models.IntegerField()
    
    def __str__(self):
        return str(self.id) + " " + self.cliente.username
    
class Detalle(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    
    def __str__(self):
        return str(self.venta.id)+" "+self.producto.descripcion
    
    
class UsuarioSuscrito(models.Model):
    usuario = Suscripcion.user
    correo_suscrito = models.EmailField(max_length=254, default="example@something.com")
    suscrito = Suscripcion.suscrito
    
    def __str__(self):
        return self.correo_suscrito
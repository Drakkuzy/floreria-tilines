from django.db import models
from django.utils import timezone

class Suscripcion(models.Model):
    user = models.CharField(max_length=100)
    correo_suscrito = models.EmailField(max_length=254, default="example@something.com")
    suscrito = models.BooleanField(default=False)
    fecha = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.user+" "+str(self.suscrito)

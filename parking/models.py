from django.db import models
from django.contrib.auth.models import User

class Propietario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    celular = models.CharField(max_length=15)
    placa_carro = models.CharField(max_length=10)
    color_carro = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
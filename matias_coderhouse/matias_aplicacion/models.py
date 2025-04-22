from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    puntos = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.nombre

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares')

    def __str__(self):
        return f"Avatar de {self.user.username}"
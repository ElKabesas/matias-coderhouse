from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    puntos = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.nombre

from django.db import models
from django.contrib.auth.models import User

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes_juegos', null=True)

    def __str__(self):
        return f'Juego ({self.id}): {self.genero} - {self.nombre}'
    
class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    lanzamiento = models.IntegerField()

    def __str__(self):
        return f'Consola ({self.id}): {self.nombre} (Lanzamiento: {self.lanzamiento})'
    
class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} ({self.pais})'
    
from django.db import models

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return f'Juego ({self.id}): {self.genero} - {self.nombre}'
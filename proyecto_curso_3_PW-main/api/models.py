from django.db import models

class Libro(models.Model):
    """

    Modelo que representa la estructura de datos de un 
    registro correspondiente a un libro en base de datos
    """

    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    publicacion = models.DateField(auto_created=True)
    precio_venta = models.BigIntegerField()

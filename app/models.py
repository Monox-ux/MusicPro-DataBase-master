from django.db import models


class app(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()


class Producto(models.Model):
    serie = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)




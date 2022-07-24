from django.db import models

# Create your models here.

class Producto(models.Model):
    tipo = models.CharField(max_length=255)
    precio = models.FloatField()

    def __str__(self):
        return f'Producto{self.id}: {self.tipo} {self.precio}'


class Alimentacion(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    foto = models.ImageField(upload_to='static/img')
    Producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Alimentacion {self.id}: {self.nombre} {self.fecha} {self.foto}'
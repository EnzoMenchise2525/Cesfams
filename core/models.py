from django.db import models

# Create your models here.
class Datos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)

    def __str__ (self):
        return self.nombre


class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class ResetaP(models.Model):
    nombre_Completo = models.CharField(max_length=50)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    fecha_Consumo = models.DateField()

    def __str__(self):
        return self.nombre_Completo


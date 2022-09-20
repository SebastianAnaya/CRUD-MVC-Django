from unittest.util import _MAX_LENGTH
from django.db import models

# Creacion de tabla para tipo de documeto
class Tipo_documento(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion= models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# Creacion de tabla para ciudad 
class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion= models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    id_tipo_documento= models.ForeignKey(Tipo_documento, on_delete=models.CASCADE)
    documento = models.IntegerField()
    lugar_de_residencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(auto_now_add =False)
    correo = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    usuario =  models.CharField(max_length=20)
    password = models.CharField(max_length=20)
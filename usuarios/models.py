
from unittest.util import _MAX_LENGTH
from django.db import models

# Creacion de tabla para tipo de documeto
class tipo_documento(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion= models.TextField(blank=True)

# Creacion de tabla para ciudad 
class ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion= models.TextField(blank=True)

class persona(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    id_tipo_documento= models.ForeignKey(tipo_documento, on_delete=models.CASCADE)
    documento = models.IntegerField()
    lugar_de_residencia = models.ForeignKey(ciudad, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(auto_now_add =False)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    usuario =  models.CharField(max_length=20)
    password = models.CharField(max_length=20)

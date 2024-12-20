from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

class Usuario(models.Model):
    dni = models.CharField(max_length=20, primary_key=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)
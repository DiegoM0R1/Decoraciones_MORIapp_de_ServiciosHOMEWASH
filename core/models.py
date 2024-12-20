from django.db import models
from users.models import Usuario
# Create your models here.
class ConfiguracionSistema(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=50, unique=True)
    valor = models.TextField()
    descripcion = models.TextField()
    tipo_valor = models.CharField(max_length=20)
    fecha_modificacion = models.DateTimeField(auto_now=True)

class RegistroActividad(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('users.Usuario', on_delete=models.CASCADE)
    tipo_actividad = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    detalles = models.JSONField()


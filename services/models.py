from django.db import models
from products.models import Producto
from sales.models import Venta

# Create your models here.
class TipoServicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Servicio(models.Model):
    sp_codigo = models.CharField(max_length=20, primary_key=True)
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class MaterialServicio(models.Model):
    id = models.AutoField(primary_key=True)
    servicio = models.ForeignKey('services.Servicio', on_delete=models.CASCADE)
    producto = models.ForeignKey('products.Producto', on_delete=models.CASCADE)
    cantidad_requerida = models.DecimalField(max_digits=10, decimal_places=2)
    obligatorio = models.BooleanField(default=True)

class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.ForeignKey('EspecialidadPersonal', on_delete=models.PROTECT)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class EspecialidadPersonal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

class DisponibilidadPersonal(models.Model):
    id = models.AutoField(primary_key=True)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.BooleanField(default=True)

class CalificacionServicio(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey('sales.Venta', on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

from django.db import models
from users.models import Usuario
# Create your models here.
class EstadoCotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

class Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha_solicitud = models.DateTimeField()
    descripcion = models.TextField()
    estado_cotizacion = models.ForeignKey(EstadoCotizacion, on_delete=models.PROTECT)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    comentario = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

class DetalleCotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    sp_codigo = models.CharField(max_length=20)  # Puede ser servicio o producto
    tipo = models.CharField(max_length=1)  # 'S' para servicio, 'P' para producto
    cantidad = models.IntegerField()
precio_estimado = models.DecimalField(max_digits=10, decimal_places=2)

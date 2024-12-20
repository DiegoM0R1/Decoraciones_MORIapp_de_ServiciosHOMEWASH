from django.db import models
from users.models import Usuario
from transactions.models import Transaccion
# Create your models here.
class EstadoVenta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

class MetodoPago(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

class TipoDescuento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField(default=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha_compra = models.DateTimeField()
    costo_total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_descuento = models.ForeignKey(TipoDescuento, on_delete=models.PROTECT, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    estado_venta = models.ForeignKey(EstadoVenta, on_delete=models.PROTECT)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)
    transaccion = models.ForeignKey(Transaccion, on_delete=models.PROTECT)
    comentario = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    sp_codigo = models.CharField(max_length=20)  # Puede ser servicio o producto
    tipo = models.CharField(max_length=1)  # 'S' para servicio, 'P' para producto
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)


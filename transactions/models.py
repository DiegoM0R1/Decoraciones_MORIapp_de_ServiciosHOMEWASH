from django.db import models

# Create your models here.
class TipoTransaccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

class Transaccion(models.Model):
    codigo_transaccion = models.CharField(max_length=50, primary_key=True)
    tipo_transaccion = models.ForeignKey(TipoTransaccion, on_delete=models.PROTECT)
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_transaccion = models.DateTimeField()
    api_response = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=True)

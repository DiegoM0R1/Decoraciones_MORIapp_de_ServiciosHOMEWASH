from django.db import models
from services.models import Servicio
# Create your models here.
class ZonaCobertura(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tarifa_adicional = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

class ServicioZona(models.Model):
    id = models.AutoField(primary_key=True)
    servicio = models.ForeignKey('services.Servicio', on_delete=models.CASCADE)
    zona = models.ForeignKey(ZonaCobertura, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Producto(models.Model):
    sp_codigo = models.CharField(max_length=20, primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

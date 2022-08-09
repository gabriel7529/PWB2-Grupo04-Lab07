from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_unidad = models.DecimalField(decimal_places=2,max_digits=5)
    precio_paquete = models.DecimalField(decimal_places=2,max_digits=5)
    fecha_carga = models.DateField(auto_now=True)
    fecha_vencimiento = 	models.DateTimeField();


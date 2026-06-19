from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock_actual = models.IntegerField(default=0)
    stock_minimo_alerta = models.IntegerField(default=5)
    precio_costo = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.stock_actual})"
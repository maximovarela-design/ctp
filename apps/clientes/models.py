from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"

class Lavado(models.Model):
    OPCIONES_TIPO = [
        ('Simple', 'Lavado Simple'),
        ('Completo', 'Lavado Completo'),
        ('Premium', 'Lavado Premium'),
    ]
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, related_name='lavados')
    tipo_lavado = models.CharField(max_length=20, choices=OPCIONES_TIPO, default='Simple')
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_lavado} - {self.vehiculo.patente}"
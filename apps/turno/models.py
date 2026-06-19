from django.db import models
from apps.clientes.models import Vehiculo

class Turno(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Terminado', 'Terminado'),
        ('Cancelado', 'Cancelado'),
    ]
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, related_name='turnos')

    def __str__(self):
        return f"Turno: {self.fecha} {self.hora} - {self.vehiculo.patente if self.vehiculo else 'Sin Auto'}"
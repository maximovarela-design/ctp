from django.contrib import admin
from .models import Turno

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'vehiculo', 'estado')
    list_filter = ('estado', 'fecha')
    ordering = ('fecha', 'hora')
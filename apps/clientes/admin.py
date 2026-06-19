from django.contrib import admin
from .models import Cliente, Vehiculo, Lavado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono')
    search_fields = ('nombre', 'apellido')
    ordering = ('apellido',)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'modelo', 'cliente')
    search_fields = ('patente', 'marca')
    list_filter = ('marca',)

@admin.register(Lavado)
class LavadoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'tipo_lavado', 'precio', 'fecha_ingreso')
    list_filter = ('tipo_lavado', 'fecha_ingreso')
    ordering = ('-fecha_ingreso',) 
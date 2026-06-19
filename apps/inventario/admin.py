from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'stock_actual', 'stock_minimo_alerta', 'precio_costo')
    search_fields = ('nombre',)
    ordering = ('stock_actual',)
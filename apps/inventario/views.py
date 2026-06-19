
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto


class ProductoListView(ListView):
    model = Producto
    template_name = 'inventario/list.html'
    context_object_name = 'productos'


class ProductoCreateView(CreateView):
    model = Producto
    fields = '__all__'
    template_name = 'inventario/create.html'
    success_url = reverse_lazy('listar_productos')


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = '__all__'
    template_name = 'inventario/update.html'
    success_url = reverse_lazy('listar_productos')


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'inventario/delete.html'
    success_url = reverse_lazy('listar_productos')
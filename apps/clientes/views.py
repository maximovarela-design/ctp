from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'telefono']
    template_name = 'clientes/create.html'
    success_url = reverse_lazy('listar_clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'telefono']
    template_name = 'clientes/update.html'
    success_url = reverse_lazy('listar_clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/delete.html'
    success_url = reverse_lazy('listar_clientes')
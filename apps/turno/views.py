# apps/turnos/views.py
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Turno

class TurnoListView(ListView):
    model = Turno
    template_name = 'turnos/list.html'
    context_object_name = 'turnos'

class TurnoCreateView(CreateView):
    model = Turno
    fields = '__all__'
    template_name = 'turnos/create.html'
    success_url = reverse_lazy('listar_turnos')
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TurnoListView.as_view(), name='listar_turnos'),
    path('nuevo/', views.TurnoCreateView.as_view(), name='crear_turno'),
]
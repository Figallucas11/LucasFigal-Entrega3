from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('agregar/', views.crear_juego, name='agregar_juego'),
    path('lista/', views.lista_juegos, name='lista_juegos'),
]
from django.urls import path
from inicio.views import inicio, lista, agregar_juego

urlpatterns = [
    path('', inicio),
    path('lista/', lista),
    path('agregar-juego/<genero>/<nombre>/', agregar_juego),
]
from django.urls import path
from inicio.views import inicio, lista

urlpatterns = [
    path('', inicio),
    path('lista/', lista)
]
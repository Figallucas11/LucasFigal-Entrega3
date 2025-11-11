from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Juego

#pagina Home
def inicio(request):
    return render(request, 'inicio.html')

#pagina para crear entradas

def agregar_juego(request, genero, nombre):
    juego = Juego(genero=genero, nombre=nombre)
    juego.save()

    return render(request, 'agregar-juego.html', {'juego1' : juego})

#pagina para visualizar la lista completa

def lista(request):

    juegos = Juego.objects.all()

    return render(request, 'lista.html', {'lista_de_juegos': juegos })

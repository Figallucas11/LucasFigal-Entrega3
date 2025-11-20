from django.shortcuts import render, redirect
from .forms import JuegoForm
from .models import Juego

# VISTA PARA EL INICIO
def inicio(request):
    return render(request, 'inicio.html')

# VISTA PARA CARGAR EL FORMULARIO 
def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_juegos') 
    else:
        form = JuegoForm()
    return render(request, 'agregar-juego.html', {'form': form})

# VISTA PARA MOSTRAR LA LISTA
def lista_juegos(request):
    juegos_guardados = Juego.objects.all()
    return render(request, 'lista.html', {'juegos': juegos_guardados})
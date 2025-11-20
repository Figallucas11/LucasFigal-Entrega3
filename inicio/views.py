from django.shortcuts import render, redirect
from .forms import JuegoForm, ConsolaForm, EmpresaForm
from .models import Juego, Consola, Empresa

# VISTA PARA EL INICIO
def inicio(request):
    return render(request, 'inicio.html')

# VISTA PARA CARGAR UN JUEGO 
def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_juegos') 
    else:
        form = JuegoForm()
    return render(request, 'agregar-juego.html', {'form': form})

# VISTA PARA CARGAR UNA CONSOLA
def crear_consola(request):
    if request.method == 'POST':
        form = ConsolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_consolas')
    else:
        form = ConsolaForm()
    
    return render(request, 'agregar_consola.html', {'form': form})

# VISTA PARA CARGAR UNA EMPRESA
def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm()
        
    return render(request, 'agregar_empresa.html', {'form': form})


# VISTA PARA VER LA LISTA DE JUEGOS
def lista_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'lista.html', {'juegos': juegos})

# VISTA PARA VER LA LISTA DE CONSOLAS
def lista_consolas(request):
    consolas = Consola.objects.all()
    return render(request, 'lista_consolas.html', {'consolas': consolas})

# VISTA PARA VER LA LISTA DE EMPRESAS
def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'lista_empresas.html', {'empresas': empresas})

# VISTA PARA BUSCAR UN JUEGO
def buscar_juego(request):
    busqueda = request.GET.get('busqueda', None)
    
    if busqueda:
        resultados = Juego.objects.filter(nombre__icontains=busqueda)
    else:
        resultados = [] # Muestra lista vacía si no hay búsqueda
        
    return render(request, 'buscar_juego.html', {'resultados': resultados, 'termino_buscado': busqueda})

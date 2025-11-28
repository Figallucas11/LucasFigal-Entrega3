from django.shortcuts import render, redirect
from .forms import JuegoForm, ConsolaForm, EmpresaForm
from .models import Juego, Consola, Empresa
from django.http import HttpResponse
from django.views.generic import UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# VISTA PARA EL INICIO
def inicio(request):
    return render(request, 'inicio.html')

# VISTA PARA CARGAR UN JUEGO 
@login_required
def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            genero = form.cleaned_data.get('genero')
            imagen = form.cleaned_data.get('imagen') 

            Juego.objects.create(
                nombre=nombre,
                genero=genero,
                imagen=imagen
            )
            return redirect('lista_juegos') 
    else:
        form = JuegoForm()
    return render(request, 'agregar-juego.html', {'form': form})

# VISTA PARA CARGAR UNA CONSOLA
@login_required
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
@login_required
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
        resultados = []
        
    return render(request, 'buscar_juego.html', {'resultados': resultados, 'termino_buscado': busqueda})

def buscar_consola(request):
    busqueda = request.GET.get('busqueda', None)
    
    if busqueda:
        resultados = Consola.objects.filter(nombre__icontains=busqueda)
    else:
        resultados = []
        
    return render(request, 'buscar_consola.html', {'consolas': resultados, 'termino_buscado': busqueda})


def buscar_empresa(request):
    busqueda = request.GET.get('busqueda', None)
    
    if busqueda:
        resultados = Empresa.objects.filter(nombre__icontains=busqueda)
    else:
        resultados = []
        
    return render(request, 'buscar_empresa.html', {'empresas': resultados, 'termino_buscado': busqueda})

# --- EMPRESA ---

# VISTA DE DETALLE
class VerEmpresa(DetailView):
    model = Empresa
    template_name = 'detalle_empresa.html'
    context_object_name = 'empresa' 

# VISTA DE EDICIÓN
class ActualizarEmpresa(LoginRequiredMixin, UpdateView):
    model = Empresa
    template_name = 'editar_empresa.html' 
    fields = '__all__'
    success_url = reverse_lazy('lista_empresas')

# VISTA DE ELIMINACIÓN
class EliminarEmpresa(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'borrar_empresa.html'
    success_url = reverse_lazy('lista_empresas')


# --- JUEGO ---

# VISTA DE DETALLE
class VerJuego(DetailView):
    model = Juego
    template_name = 'detalle_juego.html'
    context_object_name = 'juego'

# VISTA DE EDICIÓN
class ActualizarJuego( LoginRequiredMixin, UpdateView):
    model = Juego
    template_name = 'editar_juego.html'
    fields = '__all__'
    success_url = reverse_lazy('lista_juegos')

# VISTA DE ELIMINACIÓN
class EliminarJuego(LoginRequiredMixin, DeleteView):
    model = Juego
    template_name = 'borrar_juego.html'
    success_url = reverse_lazy('lista_juegos')


# --- CONSOLA ---

# VISTA DE DETALLE
class VerConsola(DetailView):
    model = Consola
    template_name = 'detalle_consola.html'
    context_object_name = 'consola'

# VISTA DE EDICIÓN
class ActualizarConsola(LoginRequiredMixin, UpdateView):
    model = Consola
    template_name = 'editar_consola.html'
    fields = '__all__'
    success_url = reverse_lazy('lista_consolas')

# VISTA DE ELIMINACIÓN
class EliminarConsola(LoginRequiredMixin, DeleteView):
    model = Consola
    template_name = 'borrar_consola.html'
    success_url = reverse_lazy('lista_consolas')
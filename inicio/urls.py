from django.urls import path
from . import views

urlpatterns = [
    # RUTA BASE
    path('', views.inicio, name='inicio'),
    
    # 1. RUTAS DE INSERCIÓN (3 formularios requeridos)
    path('agregar-juego/', views.crear_juego, name='agregar_juego'),
    path('agregar-consola/', views.crear_consola, name='agregar_consola'), # RUTA NUEVA
    path('agregar-empresa/', views.crear_empresa, name='agregar_empresa'), # RUTA NUEVA
    
    # 2. RUTAS DE LISTADO (3 listados para verificar inserción)
    path('lista/', views.lista_juegos, name='lista_juegos'),
    path('lista-consolas/', views.lista_consolas, name='lista_consolas'), # RUTA NUEVA
    path('lista-empresas/', views.lista_empresas, name='lista_empresas'), # RUTA NUEVA
    
    # 3. RUTA DE BÚSQUEDA
    path('buscar/', views.buscar_juego, name='buscar_juego'),
]
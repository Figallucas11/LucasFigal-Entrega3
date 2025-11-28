from django.urls import path
from inicio.views import (
    inicio, 
    crear_juego, 
    crear_consola, 
    crear_empresa, 
    lista_juegos, 
    lista_consolas, 
    lista_empresas,
    buscar_juego,
    VerEmpresa,
    ActualizarEmpresa, 
    EliminarEmpresa,
    VerJuego,             
    ActualizarJuego,
    EliminarJuego,
    VerConsola,           
    ActualizarConsola,
    EliminarConsola,
)
urlpatterns = [
    # ---------------------------------------------------------
    # RUTAS DE INSERCIÓN (Nombres de URL y Vistas ajustadas a 'crear')
    # ---------------------------------------------------------
    path('', inicio, name='inicio'),
    path('crear-juego/', crear_juego, name='crear_juego'), # Cambiado a crear_juego
    path('crear-consola/', crear_consola, name='crear_consola'), # Cambiado a crear_consola
    path('crear-empresa/', crear_empresa, name='crear_empresa'), # Cambiado a crear_empresa

    # ---------------------------------------------------------
    # RUTAS DE LISTADO Y BÚSQUEDA (Mantienen el nombre)
    # ---------------------------------------------------------
    path('lista-juegos/', lista_juegos, name='lista_juegos'),
    path('lista-consolas/', lista_consolas, name='lista_consolas'),
    path('lista-empresas/', lista_empresas, name='lista_empresas'),
    path('buscar-juego/', buscar_juego, name='buscar_juego'),
    # --- EMPRESA ---
    # Detalle (Ver)
    path('ver-empresa/<int:pk>/', VerEmpresa.as_view(), name='ver_empresa'),
    # Actualizar
    path('actualizar-empresa/<int:pk>/', ActualizarEmpresa.as_view(), name='actualizar_empresa'),
    # Eliminar
    path('eliminar-empresa/<int:pk>/', EliminarEmpresa.as_view(), name='eliminar_empresa'),

    # --- JUEGO ---
    # Detalle (Ver)
    path('ver-juego/<int:pk>/', VerJuego.as_view(), name='ver_juego'),
    # Actualizar
    path('actualizar-juego/<int:pk>/', ActualizarJuego.as_view(), name='actualizar_juego'),
    # Eliminar
    path('eliminar-juego/<int:pk>/', EliminarJuego.as_view(), name='eliminar_juego'),
    
    # --- CONSOLA ---
    # Detalle (Ver)
    path('ver-consola/<int:pk>/', VerConsola.as_view(), name='ver_consola'),
    # Actualizar
    path('actualizar-consola/<int:pk>/', ActualizarConsola.as_view(), name='actualizar_consola'),
    # Eliminar
    path('eliminar-consola/<int:pk>/', EliminarConsola.as_view(), name='eliminar_consola'),
]
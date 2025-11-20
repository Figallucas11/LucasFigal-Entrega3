from django.contrib import admin

from .models import Juego, Consola, Empresa

@admin.register(Consola)
class ConsolaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "lanzamiento"]
    list_filter = ["lanzamiento"] 
    ordering = ["-lanzamiento"] 
    search_fields = ["nombre"] 

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "genero"]
    list_filter = ["genero"]
    ordering = ["nombre"] 
    search_fields = ["nombre", "genero"] 

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "pais"]
    list_filter = ["pais"] 
    ordering = ["nombre"] 
    search_fields = ["nombre", "pais"]
from django import forms
from .models import Juego, Consola, Empresa 

class JuegoForm(forms.Form):
    nombre = forms.CharField(max_length=100) 
    genero = forms.CharField(max_length=50)
    imagen = forms.ImageField(required=False) 

class ConsolaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    lanzamiento = forms.IntegerField(widget=forms.NumberInput) 

class EmpresaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=50)

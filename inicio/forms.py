from django import forms
from .models import Juego, Consola, Empresa

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre', 'genero'] 

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = ['nombre', 'lanzamiento'] 

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'pais']
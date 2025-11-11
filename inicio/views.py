from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'inicio.html')

def lista(request):
    return render(request, 'lista.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria


def index(request):
    return HttpResponse("Hola Mundo")

def contacto(request, nombre):
    return HttpResponse(f"Bienvenido {nombre} a la clase de Django")

def categoria(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias.html", {"categorias": categorias})

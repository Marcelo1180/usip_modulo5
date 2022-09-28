from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Categoria
from .models import Producto
from .forms import ProductoForm 


def index(request):
    return HttpResponse("Hola Mundo")

def contacto(request, nombre):
    return HttpResponse(f"Bienvenido {nombre} a la clase de Django")

def categoria(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        categorias = Categoria.objects.all()
    print(categorias.query)
    return render(request, "categorias.html", {"categorias": categorias})

def productoFormView(request):
    form = ProductoForm()
    producto = None
    
    id_producto = request.GET.get('id')
    if id_producto:
        # producto = Producto.objects.get(id=id_producto)
        producto = get_object_or_404(Producto, id=id_producto)
        form = ProductoForm(instance=producto)

    if request.method == 'POST':
        if producto:
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "form_productos.html", {"form": form})


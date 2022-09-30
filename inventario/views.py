from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Categoria
from .models import Producto
from .forms import ProductoForm 
from .serializers import CategoriaSerializer
from .serializers import ProductoSerializer
from .serializers import ReporteProductosSerializer
from .serializers import ContactSerializer
from .permissions import IsUserAlmacen
from .utils import permission_required
import logging


logger = logging.getLogger(__name__)
# logger = logging.getLogger("Nombre personalizado")

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


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsUserAlmacen]

@permission_classes([IsAuthenticated])
class CategoriaCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
@permission_required(["inventario.reporte_cantidad"])
def categoria_contador(request):
    """
    Cantidad de items en el modelo categoria
    """
    logger.info("Cantidad categoria mostada correctamente")
    try:
        cantidad = Categoria.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def productos_tipo_unidad(request):
    """
    Productos filtrados por tipo de unidad
    """
    try:
        productos = Producto.objects.filter(unidades='u')
        return JsonResponse(
            ProductoSerializer(productos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_productos(request):
    """
    Reporte de productos
    """
    try:
        productos = Producto.objects.filter(unidades='u')
        cantidad = productos.count()

        return JsonResponse(
            ReporteProductosSerializer({
                "cantidad": cantidad,
                "productos": productos
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["POST"])
def enviar_mensaje(request):
    """
    Enviar mensajes via email
    """
    cs = ContactSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse({"mensaje": "Mensaje enviado satisfactoriamente"}, status=200)
    else:
        return JsonResponse({"mensaje": cs.errors}, status=200)

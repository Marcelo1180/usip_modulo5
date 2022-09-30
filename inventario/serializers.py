from rest_framework import serializers
from .models import Categoria
from .models import Producto
from .validators import validar_nombre_subject 


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class ReporteProductosSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    productos = ProductoSerializer(many=True)

class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=100, validators=[validar_nombre_subject,])
    body = serializers.CharField(max_length=255)

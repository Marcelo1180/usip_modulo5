from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Orden
from .models import OrdenProducto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades")
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible","precio")

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden)
admin.site.register(OrdenProducto)

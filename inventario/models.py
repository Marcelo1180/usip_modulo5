from django.db import models
from django.conf import settings
from .validators import validar_par 
from .validators import validar_nombre_categoria 
# from django.core.validators import EmailValidator 


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validar_nombre_categoria,]) 

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("reporte_cantidad", "Visualizar el reporte de cantidad"),
            ("reporte_detalle", "Reporte detallado de cantidades"),
        ]




class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    description = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10, validators=[validar_par,])
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS
    )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Producto - %s" % self.nombre

class EstadoOrden(models.TextChoices):
    NOPAGADO = 'nopagado', 'No Pagado'
    PAGADO = 'pagado', 'Pagado'

class Orden(models.Model):
    total = models.IntegerField(default=
            0)
    fecha = models.DateField()
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventario_orden_vendedor"
    )
    estado = models.CharField(
        max_length=10,
        choices=EstadoOrden.choices,
        default=EstadoOrden.NOPAGADO
    )

class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(decimal_places=2, max_digits=10)

# SELECT * FROM Categoria
# INSERT INTO Categoria ()

# SELECT * FROM Categoria WHERE nombre = "Vegetales"

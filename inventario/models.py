from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 


class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Unidades'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    description = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS
    )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

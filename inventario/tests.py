from django.test import TestCase
from .models import Categoria


class TestCategorias(TestCase):
    def test_grabacion_categorias(self):
        q = Categoria(nombre="Bebidas")
        q.save()
        self.assertEqual(Categoria.objects.count(), 1)

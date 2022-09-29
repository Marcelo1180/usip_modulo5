from django.test import TestCase
from django.test import Client
from .models import Categoria
from django.core.exceptions import ValidationError
from django.test import tag


class TestCategorias(TestCase):
    def setUp(self):
        self.client = Client()
        Categoria.objects.create(nombre="Categoria 1")
        Categoria.objects.create(nombre="Categoria 2")

    def test_grabacion_categorias(self):
        q = Categoria(nombre="Bebidas")
        q.save()
        self.assertEqual(Categoria.objects.count(), 3)

    @tag('validacion')
    def test_grabacion_categorias_no_permitido(self):
        q = Categoria.objects.create(nombre="No permitido")
        self.assertRaises(ValidationError, q.full_clean)

    @tag('validacion')
    def test_grabacion_categorias_no_permitido_mensaje(self):
        with self.assertRaises(ValidationError) as qv:
            q = Categoria.objects.create(nombre="No permitido")
            q.full_clean()

        mensaje_error = dict(qv.exception)
        self.assertEqual(mensaje_error["nombre"][0], "No es una opcion permitida")

    def test_categoria_listo(self):
        response = self.client.get('/inventario/categorias/')
        self.assertContains(response, "Categoria 1", status_code=200, html=True)

    def test_categoria_filtro(self):
        response = self.client.get('/inventario/categorias/?nombre=Categoria 2')
        self.assertNotContains(response, "Categoria 1", status_code=200, html=True)

    def test_categoria_formulario(self):
        response = self.client.post('/inventario/categorias/', {"nombre": "Categoria 3"})
        self.assertContains(response, "Categoria 3", status_code=200, html=True)

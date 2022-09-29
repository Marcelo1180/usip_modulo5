from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)


urlpatterns = [
    # path('contacto/<str:nombre>', views.contacto, name='contacto'),
    # path('', views.index, name='index'),
    # path('categorias/', views.categoria, name='categorias'),
    # path('productos/', views.productoFormView, name='productos'),
    path('categorias/cantidad', views.categoria_contador),
    path('categorias/create_list', views.CategoriaCreateAndList.as_view(), name='productos'),
    path('', include(router.urls))
]

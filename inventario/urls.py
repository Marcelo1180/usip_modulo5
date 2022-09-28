from django.urls import path
from . import views

urlpatterns = [
    # path('contacto/<str:nombre>', views.contacto, name='contacto'),
    # path('', views.index, name='index'),
    path('categorias/', views.categoria, name='categorias'),
    path('productos/', views.productoFormView, name='productos'),
]

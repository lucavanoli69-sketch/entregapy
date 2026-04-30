"""Rutas de la aplicación Blog"""

from django.urls import path
from . import views

urlpatterns = [
    # Vista principal del blog
    path('', views.home, name='home'),
    
    # Formularios de creación
    path('autor/crear/', views.crear_autor, name='crear_autor'),
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'),
    path('post/crear/', views.crear_post, name='crear_post'),
    
    # Formulario de búsqueda
    path('post/buscar/', views.buscar_post, name='buscar_post'),
]

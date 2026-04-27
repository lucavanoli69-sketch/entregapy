"""
URLs de la app Blog
Cada path conecta una URL con una función de views.py
"""

from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio - muestra todos los posts
    path('', views.home, name='home'),
    
    # URLs para crear datos
    path('autor/crear/', views.crear_autor, name='crear_autor'),
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'),
    path('post/crear/', views.crear_post, name='crear_post'),
    
    # URL para buscar posts
    path('post/buscar/', views.buscar_post, name='buscar_post'),
]

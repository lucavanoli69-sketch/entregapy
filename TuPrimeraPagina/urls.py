"""
URLs principales del proyecto TuPrimeraPagina
Aquí conectamos las URLs del proyecto con las de la app blog
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Incluimos todas las URLs de la app blog
    # Cualquier URL que no sea 'admin/' será manejada por blog/urls.py
    path('', include('blog.urls')),
]

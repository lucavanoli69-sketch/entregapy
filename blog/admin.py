"""
Registro de modelos en el panel de administración de Django
Esto permite gestionar los datos desde /admin/
"""

from django.contrib import admin
from .models import Autor, Categoria, Post

# Registramos cada modelo para que aparezca en el admin
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Post)

"""
Formularios del Blog
Cada formulario está vinculado a un modelo y genera los campos automáticamente
"""

from django import forms
from .models import Autor, Categoria, Post


# Formulario para crear un nuevo Autor
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor               # Modelo al que está vinculado
        fields = ['nombre', 'email']  # Campos que se muestran en el formulario
        labels = {
            'nombre': 'Nombre del autor',
            'email': 'Correo electrónico',
        }


# Formulario para crear una nueva Categoría
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre de la categoría',
            'descripcion': 'Descripción',
        }


# Formulario para crear un nuevo Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categoria']
        labels = {
            'titulo': 'Título del post',
            'contenido': 'Contenido',
            'autor': 'Autor',
            'categoria': 'Categoría',
        }


# Formulario de búsqueda (no está vinculado a ningún modelo, es simple)
class BuscarPostForm(forms.Form):
    # Campo de texto para ingresar el término de búsqueda
    titulo = forms.CharField(
        max_length=200,
        label='Buscar por título',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresá el título a buscar...'})
    )

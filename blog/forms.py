"""Formularios de la aplicación Blog"""

from django import forms
from .models import Autor, Categoria, Post


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']
        labels = {
            'nombre': 'Nombre del autor',
            'email': 'Correo electrónico',
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre de la categoría',
            'descripcion': 'Descripción',
        }


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


# Formulario de búsqueda
class BuscarPostForm(forms.Form):
    titulo = forms.CharField(
        max_length=200,
        label='Buscar por título',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresá el título a buscar...'})
    )

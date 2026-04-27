"""
Vistas del Blog
Cada función maneja una URL y devuelve una respuesta HTML usando templates
"""

from django.shortcuts import render, redirect
from .models import Post, Autor, Categoria
from .forms import PostForm, AutorForm, CategoriaForm, BuscarPostForm


# Vista de inicio (HOME)
# Muestra todos los posts existentes en la base de datos
def home(request):
    posts = Post.objects.all()   # Obtenemos todos los posts
    return render(request, 'home.html', {'posts': posts})


# ──────────────────────────────────────────────
# VISTAS PARA CREAR DATOS
# ──────────────────────────────────────────────

# Vista para crear un nuevo Autor
def crear_autor(request):
    if request.method == 'POST':
        # Si el usuario envió el formulario, lo procesamos
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()  # Guardamos el autor en la base de datos
            return redirect('home')  # Redirigimos al inicio
    else:
        # Si es la primera vez que entra, mostramos el formulario vacío
        form = AutorForm()
    
    return render(request, 'blog/crear_autor.html', {'form': form})


# Vista para crear una nueva Categoría
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    
    return render(request, 'blog/crear_categoria.html', {'form': form})


# Vista para crear un nuevo Post
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'blog/crear_post.html', {'form': form})


# ──────────────────────────────────────────────
# VISTA DE BÚSQUEDA
# ──────────────────────────────────────────────

# Vista para buscar posts por título
def buscar_post(request):
    form = BuscarPostForm()
    resultados = None   # Por defecto no hay resultados

    if request.method == 'POST':
        form = BuscarPostForm(request.POST)
        if form.is_valid():
            # Obtenemos el texto ingresado por el usuario
            titulo_buscado = form.cleaned_data['titulo']
            
            # Buscamos posts cuyo título contenga el texto (sin importar mayúsculas)
            resultados = Post.objects.filter(titulo__icontains=titulo_buscado)
    
    return render(request, 'blog/buscar.html', {
        'form': form,
        'resultados': resultados
    })

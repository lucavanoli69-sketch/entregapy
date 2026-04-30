"""Vistas de la aplicación Blog"""

from django.shortcuts import render, redirect
from .models import Post, Autor, Categoria
from .forms import PostForm, AutorForm, CategoriaForm, BuscarPostForm


# Vista principal del blog
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


# ──────────────────────────────────────────────
# Vistas de creación (CRUD)
# ──────────────────────────────────────────────

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    
    return render(request, 'blog/crear_autor.html', {'form': form})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    
    return render(request, 'blog/crear_categoria.html', {'form': form})


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
# Formulario de búsqueda
# ──────────────────────────────────────────────

def buscar_post(request):
    form = BuscarPostForm()
    resultados = None

    if request.method == 'POST':
        form = BuscarPostForm(request.POST)
        if form.is_valid():
            titulo_buscado = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo_buscado)
    
    return render(request, 'blog/buscar.html', {
        'form': form,
        'resultados': resultados
    })

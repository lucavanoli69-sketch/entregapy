"""
Modelos del Blog
Aquí definimos las tablas de la base de datos usando clases de Python
"""

from django.db import models


# Modelo 1: Autor
# Representa a las personas que escriben en el blog
class Autor(models.Model):
    nombre = models.CharField(max_length=100)   # Nombre del autor
    email = models.EmailField(unique=True)       # Email único por autor

    def __str__(self):
        # Esto define cómo se muestra el objeto en el admin y en templates
        return self.nombre

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


# Modelo 2: Categoria
# Las categorías ayudan a organizar los posts del blog
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)        # Nombre de la categoría
    descripcion = models.TextField(blank=True)        # Descripción opcional

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


# Modelo 3: Post
# El contenido principal del blog
class Post(models.Model):
    titulo = models.CharField(max_length=200)         # Título del post
    contenido = models.TextField()                    # Cuerpo del post
    fecha = models.DateTimeField(auto_now_add=True)   # Se guarda automáticamente al crear
    
    # Relación con Autor (un post tiene un autor)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.SET_NULL,   # Si se borra el autor, el post queda sin autor
        null=True,
        blank=True
    )
    
    # Relación con Categoria (un post pertenece a una categoría)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,   # Si se borra la categoría, el post queda sin categoría
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-fecha']   # Los más recientes primero

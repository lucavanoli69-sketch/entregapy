# TuPrimeraPaginaVanoli

Este proyecto es una página web hecha con Django para una entrega del curso.

La idea fue armar un blog simple donde se pueden crear autores, categorías y posts, y también buscar posts por título.

---

## Cómo correr el proyecto

1. Clonar el repositorio:
git clone https://github.com/lucavanoli69-sketch/entregapy.git

2. Entrar a la carpeta:
cd TuPrimeraPaginaVanoli

3. Instalar Django (si no lo tenés):
pip install django

4. Crear la base de datos:
python manage.py makemigrations
python manage.py migrate

5. Crear usuario admin:
python manage.py createsuperuser

6. Levantar el servidor:
python manage.py runserver

7. Abrir en el navegador:
http://127.0.0.1:8000/

---

## Cómo probar la página

El orden que usé para probar todo fue:

1. Crear un autor  
2. Crear una categoría  
3. Crear un post  
4. Buscar un post  
5. Ver todo desde el inicio  

También se puede entrar al admin:
http://127.0.0.1:8000/admin/

---

## Qué tiene el proyecto

- 3 modelos (Autor, Categoría y Post)  
- Formularios para cargar datos  
- Búsqueda de posts por título  
- Templates con herencia (base.html)  
- Estructura básica de Django con patrón MVT  

---

## Tecnologías

- Python  
- Django  
- SQLite  
- HTML básico  

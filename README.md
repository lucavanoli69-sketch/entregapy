# TuPrimeraPagina - Blog en Django

Proyecto web desarrollado con Django como parte de un trabajo práctico.
Incluye un blog simple con 3 modelos, formularios para cargar datos y búsqueda.

---

##  Cómo correr el proyecto

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/TU_USUARIO/TuPrimeraPagina+Apellido.git
cd TuPrimeraPagina
```

### 2. Instalar Django

```bash
pip install django
```

### 3. Crear las tablas en la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear un superusuario (para acceder al admin)

```bash
python manage.py createsuperuser
```

### 5. Correr el servidor

```bash
python manage.py runserver
```

### 6. Abrir en el navegador

```
http://127.0.0.1:8000/
```

---

## 📋 Orden recomendado para probar las funcionalidades

1. **Crear un Autor** → http://127.0.0.1:8000/autor/crear/
2. **Crear una Categoría** → http://127.0.0.1:8000/categoria/crear/
3. **Crear un Post** → http://127.0.0.1:8000/post/crear/
4. **Buscar un Post** → http://127.0.0.1:8000/post/buscar/
5. **Ver todos los Posts** → http://127.0.0.1:8000/
6. **Panel Admin** → http://127.0.0.1:8000/admin/

---

## 🗂️ Estructura del proyecto

```
TuPrimeraPagina/
│
├── manage.py                   → Comando principal de Django
├── TuPrimeraPagina/
│   ├── settings.py             → Configuración del proyecto
│   ├── urls.py                 → URLs principales
│   └── wsgi.py / asgi.py
│
├── blog/
│   ├── models.py               → Modelos: Autor, Categoria, Post
│   ├── views.py                → Lógica de cada página
│   ├── forms.py                → Formularios
│   ├── urls.py                 → URLs de la app
│   └── admin.py                → Registro en el admin
│
├── templates/
│   ├── base.html               → Template base con navbar (herencia)
│   ├── home.html               → Página de inicio
│   └── blog/
│       ├── crear_autor.html
│       ├── crear_categoria.html
│       ├── crear_post.html
│       └── buscar.html
│
└── README.md
```

---

## 📦 Modelos

| Modelo     | Campos                              |
|------------|-------------------------------------|
| Autor      | nombre, email                       |
| Categoria  | nombre, descripcion                 |
| Post       | titulo, contenido, fecha, autor, categoria |

---

## 🔧 Tecnologías usadas

- Python 3
- Django 4+
- SQLite (base de datos por defecto)
- HTML + CSS (sin librerías externas)

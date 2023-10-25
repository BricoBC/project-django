# Empecemos a conocer el mundo de DJANGO! 🐍
Primero recordemos buenas prácticas al comenzar un proyecto en python las cuales son:

- Crear carpeta del proyecto.
```bash
  mkdir carpeta
```
- Inicializar git.
```bash
  git init
```

- Crear entorno virtual.
```python
python3 -m venv venv
```

- Activar entorno virtual.
```bash
source ./venv/bin/activate
```
- Hacer un documento txt en donde esten las dependencias que utilicemos.
```python
pip freeze > requirements.txt
```

- Instalar dependencias:
```python
pip install -r requirements.txt
```

Ya una vez que se comenzó con buenas practicas no hay que olvidar estar guardando las versiones del código en cualquier repositorio web que más conocimientos se tenga.
 ## Primeros pasos: Instalación
 Primero hay que ubicarnos en a ubicación en donde se quiere tener el proyecto, ya una vez estando en el directorio se hace lo siguiente:

 1.- Instalar django:
 ```python
python3 -m pip install Django
```

2- Verificar la versión
 ```python
python3 -m pip install Django
```

## Crear el proyecto
El proyecto va a tener como nombre **mysite**
```python
django-admin startproject mysite .
```
Se va a crear una carpeta con el nombre del proyecto y dentro de si va a tener unos ficheros con extensión python.
```
v mysite
| > __pycache__
|   __init__.py
|   asgi.py
|   settings.py
|   urls.py
|   wsgi.py
db.sqlite3
manage.py
```

- __pycache__: Es para guardar código que ya fue compilado y pueda ser ejecutado más rápido.
- __init__.py: Es para indicar que mysite es un modulo.
- asgi.py: Es para poder configurar el servicio que puede proveer django.
- **settings.py:** Es para ver toda la configuración del proyecto.
- **urls.py**: Es en donde se indica los urls que los usuarios pueden visitar.
- wsgi.py: Es para poder configurar el servicio que puede proveer django.
- db.sqlite3: Es la base de datos sql.
- manage.py: Permite ejecutar comando administrativos del proyecto. Si se necesita ver todos los comandos hay que ejecutar:
```python
python manage.py --help
```


### Ejecutar el proyecto:
 ```python
python manage.py runserver
```
En caso de tener muchos proyectos ejecutandose al mismo tiempo se puede cambiar el puerto de la siguiente forma:
 ```python
python manage.py runserver 3000
```
En el ejemplo de arriba se va a direccionar al **puerto 3000**
## Crear aplicaciones
La aplicación va a tener como nombre **myapp**
 ```python
python manage.py startapp myapp
```
Se va a crear dos carpetas, y los demás son archivos con extensión python.
```
v myapp
| > __pycache__
| > migrations
|    __init__.py
|   admin.py
|   apps.py
|   models.py
|   tests.py
|   views.py
```
- __pycache__: Es para guardar código que ya fue compilado y pueda ser ejecutado más rápido.
- migration: Es la carpeta en donde se almacena la información de la Base de datos, tiene un archivo __init__ de igual manera.
- __init__: Es para que se pueda considerar un modulo la app.
- admin: Es para configurar todo el panel de los permisos.
- apps.py: Es para poder configurar todo acerca de la aplicación.
- models.py: Es para crear las clases que posteriormente se van a crear como tablas.
- tests.py: Es para realizar el testing de las vistas o de los archivos generados.
- **views:** Es el fichero en donde se va a almacenar el código html para las vistas, lo que va a poder ver el usuario.




### Autor
[@BricoBC](https://github.com/BricoBC)

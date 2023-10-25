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


## Ejecutar el proyecto:
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


### Autor

- [@BricoBC](https://github.com/BricoBC)

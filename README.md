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
## 1) Primeros pasos: Instalación
 Primero hay que ubicarnos en a ubicación en donde se quiere tener el proyecto, ya una vez estando en el directorio se hace lo siguiente:

1. Instalar django:
 ```python
python3 -m pip install Django
```

2. Verificar la versión
 ```python
python3 -m pip install Django
```

## 2) Crear el proyecto
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

- _pycache_: Es para guardar código que ya fue compilado y pueda ser ejecutado más rápido.
- _init_.py: Es para indicar que mysite es un modulo.
- asgi.py: Es para poder configurar el servicio que puede proveer django.
- **settings.py:** Es para ver toda la configuración del proyecto.
- **urls.py**: Es en donde se indica los urls que los usuarios pueden visitar.
- wsgi.py: Es para poder configurar el servicio que puede proveer django.
- db.sqlite3: Es la base de datos sql.
- manage.py: Permite ejecutar comando administrativos del proyecto. Si se necesita ver todos los comandos hay que ejecutar:
```python
python manage.py --help
```


### 2.1) Ejecutar el proyecto:
 ```python
python manage.py runserver
```
En caso de tener muchos proyectos ejecutandose al mismo tiempo se puede cambiar el puerto de la siguiente forma:
 ```python
python manage.py runserver 3000
```
En el ejemplo de arriba se va a direccionar al **puerto 3000**
## 3) Crear aplicaciones
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
- _pycache_: Es para guardar código que ya fue compilado y pueda ser ejecutado más rápido.
- _migration_: Es la carpeta en donde se almacena la información de la Base de datos, tiene un archivo __init__ de igual manera.
- __init__: Es para que se pueda considerar un modulo la app.
- admin: Es para configurar todo el panel de los permisos.
- apps.py: Es para poder configurar todo acerca de la aplicación.
- models.py: Es para crear las clases que posteriormente se van a crear como tablas.
- tests.py: Es para realizar el testing de las vistas o de los archivos generados.
- **views:** Es el fichero en donde se va a almacenar el código html para las vistas, lo que va a poder ver el usuario.

## 4) Crear un vista
Para agregar una vista es necesario tener almenos una app y un proyecto.
1. Se accede al archivo de *__views.py__* de la app.
2. Se agrega lo siguiente al archivo:

``` python
from django.http import HttpResponse

def hi(request):
    return HttpResponse("<h1>Hello world</h1>")
```

Hay que replicar la acción previa correspondiente a las vistas que se necesiten.

3. Se crea un nuevo archivo en la carpeta de la app con el nombre de *__urls.py__*
4. Se debe de tener el siguiente código dentro del archivo creado:
``` python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi ), #Accede a la ruta, ejecuta la función.
    path('about', views)
]

```
5. Acceder al archivo _**url.py**_ del proyecto
6. Se debe de tener el siguiene código dentro del archivo:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myapp.urls") ), 
    # Recibe dos parametros:
    # 1) ruta del url
    # 2) vista del proyecto o el include para las url's de la app
    #Nota para include: la ruta final = ruta que se indique en éste archivo + la ruta que se tenga en su archivo url
]

```
7. Ejecutar el proyecto y poner la ruta, en mi caso seria de la siguiente forma el url: *http://127.0.0.1:8000/* ó *http://127.0.0.1:8000/admin* ó *http://127.0.0.1:8000/about*, depende de la cuál quieras acceder.


## 5) Crear tablas de Bases de Datos
1. Acceder al archivo de *__models.py__* de la aplicación.
2. Se debe de tener el siguiente código para poder crear una tabla:
```python
from django.db import models

# Las clases son las tablas
class Project(models.Model):
    name = models.CharField(max_length=255)
    #Los atributos con las columnas
#Tabla: Project, con la columna id y name.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #models.cascade hace que si se elimina un proyecto sus tareas también serán eliminadas.

```
A continuación dejo la documentación en donde existe los diferentes tipos de datos que puede adquierir el campo de una columna.
[Ir a Documentación...](https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types)

3. Acceder al archivo de *__settings.py__* del proyecto
4. Existe un array con el nombre de __INSTALLED_APPS__, al final hay que agregar el nombre de la aplicación, esto con el fin para poder unificar las tablas de administración y que contiene el proyecto por defecto con las que estamos creando.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp', #Está es mi aplicación
]
```
5. Ejecutar el siguiente comando:
```python
python manage.py makemigrations
```
En caso de que queremos especificar de uno solo seria:
```python
python manage.py makemigrations myapp
```
Con éste comando lo que se hace es compilar las clases.

6. Ejecutar el siguiente comando:
```python
python manage.py migrate
```
En caso de que queremos especificar de uno solo seria:
```python
python manage.py migrate myapp
```
Con éste comando se ejecuta todas las compilaciones de las clases para convertirlas en las tablas.

NOTA: Django viene por defecto con SQLite, en debido caso que se quiera modificar hay que hacer lo siguiente:

### 5.1) Cambiar base de datos 
1. Ir a *__settings.py__* del proyecto
2. Encontrar el dicionario que tiene como nombre __DATABASES__
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
3. Modificar el engine por el que se vaya a utilizar, dejo a continuación la pagina en donde se encuentra las conexiones con las demás bases de datos:
['Ir a la documentación...'](https://docs.djangoproject.com/en/4.2/ref/databases/)
 
4. Modificar el nombre de como se va a registrar la base de datos, recomiendo *'db.base_de_datos'*

*Ya para este punto existen tablas en el archivo db.sqlite3, si se quiere ver todas las tablas es necesario tener una herramienta de software que se utiliza como cliente universal para base de datos. En mi caso utilizo __dbeaver__, dejo a continuación los pasos para hacer uso de éste software gratuito.*
### 5.2) DBeaver
1. Instalar el software: [Ir a la página de descarga...](https://dbeaver.io/download/)
2. Abrir el sofware.
3. Hacer clic en el icono de un enchufe que se encuentra abajo de "File".
4. Se va abrir una pestaña nueva en donde solicita la base de datos, se va a escribir "SQLite", le damos doble clic a la primera opción que muestre.
5. Va a pedir la ubicación para indicar hay que hacer clic en "Create" y se va a localizar hasta donde encuentre el archivo correspondiente.
6. Hacer clic en "Finish"
Cuando sea tu primera vez con esa base de datos te va a indicar que se tiene que instalar el driver asi que lo permites y ya podrás visualizar la base de datos.

!['DBeaver'](https://dbeaver.io/wp-content/uploads/2015/09/beaver-head.png)

## 6) Django shell
Para ingresar los valores en las tablas se puede hacer de la siguiente forma:
1. Se ejecuta el siguiente comando:
```python
python manage.py shell
```
Ésto activara el shell de python

2. Indicar los modelos con los que vamos a trabajar.
```python
from myapp.models import Project, Task
```
### 6.1) Guardar un valor en la BD

```python
p = Project(name='Elaborar una página web')
p
p.save()
```
Recordemos que mi modelo de Project, tiene la columna de __id__ que es autoincrementable y __name__ que recibe un string.

### 6.2) Obtener un elemento
```python
Projects.objects.get(id=1)
```
Con objects.get recibe como parametro el nombre de la columna y el valor exacto que se busca obtener.

### 6.3) Filtrar
```python
Project.objects.filter(name__startswith="Elabor")
```
__output:__ *<QuerySet [<Project: Project object (1)>, <Project: Project object (2)>]>*

### 6.4) Salir de la consola
```python
exit()
```

### 6.5) Guardar un valor de una tabla conectada
En mi caso __Task__ esta relacionada a un valor que se tenga en __Project__, asi que primero debo de asignar un proyecto y después al proyecto le asigno sus tareas, por ende su código quedaria de la siguiente forma:
```python
p = Project.object.get(id=1)
#En p tiene el id 1
p.task_set.create(title="Hacer el mockup", 
           description="Usar uizard para el diseño de la pagina web")

```

Para ver todas las tareas que tiene el id 1, se hace lo siguiente:
```python
p = Project.objects.get(id=1)
p.task_set.all()
```
## 7) Recibir parametros de un url
Primero se tiene que crear una vista e indicar su url, después de tener ésto hay que considerar lo siguiente:
- El tipo de dato que tenemos que recibir
- El nombre de la variable que se va a recibir

Para saber el tipo de dato se puede saber con el siguiente método:
```python
print(type(username))
```
En mi caso quiero saber el tipo de dato de la variable __username__.

En la vista que se creó, además de recibir el request se agrega el segundo parametro.
```python
def hi(request, username):
    full = username + "_2509"
    return HttpResponse("<h1>Hello world %s</h1>" %full)
    # %s es para mandar el valor de la variable
    # %<nombre_variable> va afuera de la cadena de caracteres, es la variable que queremos enviar
```
Para los urls tiene que quedar de la siguiente forma:
```python
urlpatterns = [
    path('<str:username>/', views.hi ), 
    # < tipo_de_dato : nombre_variable >/
    path('about/', views.about)
]
```
### 7.1) Consumir base de datos desde la url
Se tiene que hacer las vistas y los urls para recibir un parametro, aunque se debe de hacer los siguientes cambios:
- Agregar las tablas que va a utilizar.
- En caso de ser necesario, agregar JsonResponse
- Agregar get_object_or_404 

__VIEWS.PY:__
```python
from django.http import HttpResponse, JsonResponse #Se agrega JsonResponse
from .models import Project, Task #Se agrega las tablas
from django.shortcuts import get_object_or_404 #método para resolver un error

def projects(reques):
    p = list(Project.objects.values())
    return JsonResponse(p, safe=False)
    #Se devuelve en formato de Json por la abundancia de caracteres ya que de esa forma no se puede mandar como un string. 

def task(reques, id):
    # task = Task.objects.get(id=id)
    # Se replicaria de la misma forma como en el shell..
    task = get_object_or_404(Task, id=id)
    # El método hace la consulta y si no existe devuelve un error 404
    # Primer parametro: Tabla
    # Segunda parametro: La columna
    return HttpResponse('Task: %s' %task.title)
    #output: Task: Titulo
```
Para el archivo de urls.py, no hay mucho cambio. Se hace el mismo procedimiento que cuando mandamos parametros en la url.

__URLS.PY__
```python
from django.urls import path
from . import views

urlpatterns = [
    path('hi/<str:username>/', views.hi ), #Accede a la ruta, ejecuta la función.
    path('about/', views.about),
    path('project/', views.projects),
    path('task/<int:id>', views.task)
]
```
## 8) Panel de administrador
En la __terminal__ se va a ejecutar lo siguiente:
```python
python manage.py createsuperuser
```
- Agrega un usuario:
- Agrega un correo:
- Agrega una contraseña:
Esto es para crear un super usuario, asi que se accede a la ruta *http://127.0.0.1:8000/admin/* e inicia sesión.

### 8.1) Registrar las tablas de la aplicación
Cuando se crea una aplicación se crea un archivo __admin.py__, aquí se va a acceder y agregar lo siguiente:
```python
from django.contrib import admin
from .models import Project, Task # Se agrega las tablas que se quiere registrar

admin.site.register(Project)
admin.site.register(Task)
#Se hace el registro de cada tabla, en mi caso la tabla Project y Taks.
```
Recargas nuevamente la página y te va a aparecer el nombre de la aplicación y las tablas que se registraron.
Accedes a la tabla dando clic al nombre de la tabla.

### Modificar la forma en como se muestra la información de la tabla
Cuando se accede a la tabla muy probablemente salga una tabla y se enliste los datos como *"Project object(1)"*, para modificar eso hay que hacer lo siguiente:
1. Se accede al archivo __models.py__
2. Localizas la clase de la tabla que se va a modificar la información, en mi caso es *__Task__*
3. Ingresas una función dentro de tu clase, así:
```python
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title + " del proyecto " + self.project.name
        # Titulo_tarea DEL PROYECTO nombre_proyecto
```
Ya sólo queda recargar la página y ver el cómo devuelve la información.


## __Autor__
[@BricoBC](https://github.com/BricoBC)

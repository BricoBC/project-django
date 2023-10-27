from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def hi(request, username):
    full_name = username + "_2509"
    return render(request, 'hello.html', {'username': full_name} )

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'project.html', {
        'projects': projects
    })

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task.html', {
        'task': task
    })
    #Lo que se manda es la fila que se consultó, en mi caso tiene la siguiente forma:
    #tasks = __str__, tasks.id, tasks.title, tasks.description, tasks.project_id, tasks.done.
    #Por ende estás propiedades se pueden utilizar a la hora de mandarlo a la plantilla

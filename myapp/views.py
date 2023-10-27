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

def task(reques, id):
    # task = Task.objects.get(id=id)
    # Se replicaria de la misma forma como en el shell..
    task = get_object_or_404(Task, id=id)
    # El método hace la consulta y si no existe devuelve un error 404
    # Primer parametro: Tabla
    # Segunda parametro: La columna
    return HttpResponse('Task: %s' %task.title)
    #output: Task: Titulo
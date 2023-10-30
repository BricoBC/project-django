from django.urls import path
from . import views

urlpatterns = [
    path('hi/<str:username>/', views.hi ), #Accede a la ruta, ejecuta la función.
    path('about/', views.about, name= 'about'),
    path('project/', views.projects, name='projects'),
    path('task/<int:id>', views.task),
    path('create_project/', views.create_new_project, name='create_new_project'),
    path('project_tasks/<int:id>/', views.project_tasks, name='project_details'),
]


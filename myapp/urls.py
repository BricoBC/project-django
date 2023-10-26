from django.urls import path
from . import views

urlpatterns = [
    path('hi/<str:username>/', views.hi ), #Accede a la ruta, ejecuta la función.
    path('about/', views.about),
    path('project/', views.projects),
    path('task/<int:id>', views.task)
]


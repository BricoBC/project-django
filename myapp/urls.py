from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.hi ), #Accede a la ruta, ejecuta la función.
    path('about/', views.about)
]


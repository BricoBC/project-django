from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi ), #Accede a la ruta, ejecuta la función.
    path('about', views.about)
]


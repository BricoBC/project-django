from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myapp.urls") ), 
    # 1) ruta del url 
    # 2) vista del proyecto o el include para las url's de la app
]

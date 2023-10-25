from django.db import models

# Las clases son las tablas
class Project(models.Model):
    name = models.CharField(max_length=255)
    #Los atributos con las columnas
#Tabla: Project, con la columna id y name.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

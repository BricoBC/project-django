from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    #Los atributos con las columnas
    
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    #Nueva columna con el titulo de Done
    #Por defecto tendrá el valor False.
    
    def __str__(self) -> str:
        return self.title + " del proyecto " + self.project.name

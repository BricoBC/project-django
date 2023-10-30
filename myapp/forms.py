from django import forms

class CreateNewProject(forms.Form):
    nombre = forms.CharField(label = 'Titulo del proyecto', max_length=200, required=True,
                            widget=forms.TextInput( attrs={ 'class': 'input' } ) )
    
class CreateNewTask(forms.Form):
    title = forms.CharField(label = 'Titulo de la tarea', max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, label="Descripción",
                                max_length=200,)
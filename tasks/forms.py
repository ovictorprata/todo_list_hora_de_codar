from dataclasses import fields
from django import forms
from .models import Task

class TaskForm(forms.ModelForm): #pra ganhar acesso aos métodos que facilitam a importação
    class Meta:
        model = Task
        fields = ('title', 'description') #apenas os dois pq os outros já tem default/preenchimento automático

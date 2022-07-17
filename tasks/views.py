from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def TaskList(request):
    tasks = Task.objects.all() #A VARIÁVEL QUE VAI RETORNAR O QUE VOCÊ QUER PARA O FRONT, o ALL RETORNA TUDO
    return render(request, 'tasks/list.html', {'tasks' : tasks})

def TaskView(request, id): #O ID vai ser passado pelo template
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task' : task})



def HelloWorld(request):
    return HttpResponse('Hello World')


def YourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})

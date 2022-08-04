from contextlib import redirect_stderr
from http.client import HTTPResponse
from turtle import title
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required




# Create your views here.


# ================================================CRUD=============================================

#CRUD - CREATE
@login_required
def NewTask(request):
    #devemos chamar o formulário, para isso importar o TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST) #joga para o front pelo formulario e já preenche

        if form.is_valid(): #testa se o formulário é válido
            task = form.save(commit=False) #vai começar a salvar a task, mas vai parar a inserção e vai ESPERAR até a gente mandar salvaer
            task.done = 'Undone'
            task.user = request.user
            task.save()
        return redirect('/')

    else: #se não for, nãoo mexe em nada
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form' : form})


#CRUD - READ
@login_required
def TaskList(request):

    search = request.GET.get('search') #o 'search é o name='' do input de busca

    if search:
        tasks = Task.objects.filter(title__icontains=search, user = request.user) #o __icontains ignora o search
    else:

        task_list = Task.objects.all().order_by('-created_at').filter(user = request.user) #A VARIÁVEL QUE VAI RETORNAR O QUE VOCÊ QUER PARA O FRONT, o ALL RETORNA TUDO

        paginator = Paginator(task_list, 10) #é o número de dados por página que você quer exibir

        page = request.GET.get('page') #é o número da página tipo: www.site.com/page/2

        tasks = paginator.get_page(page) #exibe o número correto na página correta

    return render(request, 'tasks/list.html', {'tasks' : tasks})


@login_required
def TaskView(request, id): #O ID vai ser passado pelo template
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task' : task})





#CRUD - UPDATE
@login_required
def EditTask(request, id):
    #esse Task é a tabela do models
    task = get_object_or_404(Task, pk=id)
    #preenche o formulário, o instance deixa o formulário pré populado para ajudar a editar
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if(form.is_valid()):
            task.save()
            return redirect('/')    
        else:
            return render(request, 'tasks/edit-task.html', {'form' : form, 'task' : task})
            
    else:
        return render(request, 'tasks/edit-task.html', {'form' : form, 'task' : task})


#CRUD - DELETE
@login_required
def DeleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/')


def HelloWorld(request):
    return HttpResponse('Hello World')


@login_required
def YourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})



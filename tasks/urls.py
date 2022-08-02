from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.HelloWorld),
    path('', views.TaskList),
    path('yourname/<str:name>', views.YourName, name='your-name'),
    path('new-task/', views.NewTask, name='new-task'),
    path('task/<int:id>', views.TaskView, name="task-view"),
    path('edit/<int:id>', views.EditTask, name='edit-task'),
    path('delete/<int:id>', views.DeleteTask, name='delete-task'),
]

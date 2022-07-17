from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.HelloWorld),
    path('', views.TaskList),
    path('yourname/<str:name>', views.YourName, name='your-name'),
    path('task/<int:id>', views.TaskView, name="task-view")
]

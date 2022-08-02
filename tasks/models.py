from pyexpat import model
from ssl import create_default_context
from telnetlib import STATUS
from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS = (
        ('Undone', 'Undone'),
        ('Done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=6, choices=STATUS,) #lista os tipos de opções do usuário
    created_at = models.DateTimeField(auto_now_add=True) #sempre que for criado, o valor de dada vai ser criado no banco
    updated_at = models.DateTimeField(auto_now=True) #pega a hora da atualização

    def __str__(self):
        return self.title
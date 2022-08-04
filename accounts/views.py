from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy #é igual o redirect, mas qnd usa classe do Based View, precisa de usar ele
from django.views import generic #deixa criar uma class do BasedView


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') #onde o usuário será redirecionado em caso de sucesos no login
    template_name = 'registration/register.html'

from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegistroForm

class RegistroUsuarioView(generic.CreateView):
    form_class=RegistroForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

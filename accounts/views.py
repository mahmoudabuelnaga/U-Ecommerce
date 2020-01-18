from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView , FormView

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')

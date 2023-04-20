from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from login.forms import LoginForm


class LoginUserView(LoginView):
    template_name = 'login/login.html'
    form_class = LoginForm

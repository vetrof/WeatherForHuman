from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from registration.forms import UserRegistrationForm
from users.models import User


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'login/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы, успешно зарегистрированы!'

from django.shortcuts import render
from .models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class UserListView(ListView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'email']


class UserUpdateView(UpdateView):
    model = User

    fields = ['first_name', 'last_name', 'email']


class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

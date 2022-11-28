from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomUserChangeForm


def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Неверные данные"))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {'title': 'Login Page', })


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ('Успешная регистрация!'))
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/register.html', {'title': 'Регистрация', 'form': form})


def user_page(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            messages.success(request, ('Успешно!'))
            return redirect('home')
        messages.error(request, "Что-то пошло не так.")
    else:
        form = CustomUserCreationForm(instance=request.user)
    return render(request, 'user_page/user_page.html', {'title': 'Изменение данных пользователя', 'form': form})
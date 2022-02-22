from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate
from django.shortcuts import render, redirect
from .forms import *


def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('posts')

        else:

            messages.error(request, 'Login yoki parol xato!!! Qaytadan urinib koring')

            return redirect('login')

    return render(request, 'accounts/login.html')


def user_register(request):
    if request.POST:
        form = RegistrationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            username = form.save()

            return redirect('login')

        else:
            messages.error(request, 'Xato kiritdingiz! yoki bunday foydalanuvchi ro\'yxatdan o\'tgan')

            return redirect('register')

    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def log_out(request):
    logout(request)

    return redirect('posts')
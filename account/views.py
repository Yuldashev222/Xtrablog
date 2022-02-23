from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate
from django.shortcuts import render, redirect

from post.forms import *
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
    print(1)
    if request.POST:
        print(2)
        form = RegistrationForm(request.POST)

        if form.is_valid():
            print(3)
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


def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)

    post_form = PostForm()

    if request.POST:
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            obj = post_form.save(commit=False)
            author = User.objects.filter(username=username).first()
            obj.author = author
            obj.save()
            post_form.save()

            return redirect('profile', request.user.username)

    context = {
        'profile': user,
        'post_form': post_form,
        'posts': posts,
    }

    return render(request, 'accounts/profile.html', context=context)

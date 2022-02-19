from django.shortcuts import render
from django.views.generic.base import View

from .models import *


class PostsView(View):
    """ Posts List """

    def get(self, request):
        posts = Post.objects.all()
        context = {
            'title': 'Posts',
            'posts': posts,
        }
        return render(request, 'post/index.html', context=context)


class PostDetailView(View):
    """ Post single """

    def get(self, request, slug):
        post = Post.objects.get(url=slug)
        context = {
            'post': post,
        }
        return render(request, 'post/post.html', context=context)


class AboutView(View):
    """ About """

    def get(self, request):
        context = {
            'title': 'About Us',
        }
        return render(request, 'about.html', context=context)


class ContactView(View):
    """ Contact """

    def get(self, request):
        context = {
            'title': 'Contacts',
        }
        return render(request, 'contact.html', context=context)


class PostView(View):
    """ Posts List """

    def get(self, request):
        posts = Post.objects.all()
        context = {
            'title': 'Post',
            'posts': posts,
        }
        return render(request, 'post/post.html', context=context)

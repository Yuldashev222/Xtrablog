from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View

from mainapp.forms import *
from .forms import *
from .models import *


def posts(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query)).order_by(
            '-date_update')

    else:
        posts = Post.objects.filter(active=True).order_by('-date_update')

    cats = Category.objects.all()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Posts',
        'posts': posts,
        'cats': cats,
        'obj': page_obj
    }

    return render(request, 'post/index.html', context=context)


def filter_posts(request, slug):
    search_query = request.GET.get('search', '')

    cats = Category.objects.all()
    category = Category.objects.get(url=slug)

    if search_query:
        fil_posts = Post.objects.filter((Q(title__icontains=search_query) | Q(text__icontains=search_query)), category=category, active=True).order_by('-date_update')

    else:
        fil_posts = Post.objects.filter(category=category, active=True).order_by('-date_update')

    paginator = Paginator(fil_posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Posts',
        'category': category,
        'filter_posts': fil_posts,
        'cats': cats,
        'obj': page_obj,
    }

    return render(request, 'post/filter_in_category_posts.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, url=slug)
    posts = Post.objects.filter(category=post.category, active=True)
    comments = Comment.objects.filter(post=post).order_by('-date')
    comment_form = CommentForm

    if request.POST:
        if request.user.is_authenticated:
            comment = CommentForm(request.POST)
            if comment.is_valid():

                comment = comment.save(commit=False)
                comment.author = request.user
                comment.post = post

                comment.save()

            else:

                print('formada xatolik bor')
    context = {
        'form': comment_form,
        'post': post,
        'posts': posts,
        'comments': comments,
    }

    return render(request, 'post/post_detail.html', context)


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

    def post(self, request):
        message = MessagesForm

        if request.POST:
            if request.user.is_authenticated:
                message = MessagesForm(request.POST)
                if message.is_valid():
                    message = message.save(commit=True)
                    message.user = request.user
                    message.save()

                else:
                    print('/?/???//??')

            elif message.is_valid():
                message = message.save(commit=True)
                message.save()

            else:
                print('/?/???//??')

        context = {
            'title': 'Contacts',
        }

        return render(request, 'contact.html', context=context)


class PostView(View):
    """ Posts List """

    def get(self, request):
        post = Post.objects.filter(active=True).order_by('-date_update')[0]
        comments = Comment.objects.filter(post=post).order_by('-date')

        context = {
            'title': 'Last Post',
            'post': post,
            'comments': comments,
        }
        return render(request, 'post/post.html', context=context)

    def post(self, request):
        post = Post.objects.filter(active=True).order_by('-date_update')[0]

        comments = Comment.objects.filter(post=post).order_by('-date')

        if request.POST:
            if request.user.is_authenticated:
                comment = CommentForm(request.POST)
                if comment.is_valid():

                    comment = comment.save(commit=False)
                    comment.author = request.user
                    comment.post = post

                    comment.save()

                else:

                    print('formada xatolik bor')

        context = {
            'title': 'Last Post',
            'post': post,
            'comments': comments,
        }

        return render(request, 'post/post.html', context=context)

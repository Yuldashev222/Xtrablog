from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc']


@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'image', 'date_created', 'date_update', 'active']


@admin.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'parent', 'author', 'date']

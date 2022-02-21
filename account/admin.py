from django.contrib import admin

from .models import *


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'photo']


@admin.register(Employee)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'info', 'position']

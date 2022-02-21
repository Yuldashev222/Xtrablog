from django.contrib import admin

from .models import *


@admin.register(AboutUs)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'telegram_link', 'instagram_link', 'facebook_link']


@admin.register(Messages)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email', 'subject']

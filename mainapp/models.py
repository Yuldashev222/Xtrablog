from django.db import models

from account.models import User


class Messages(models.Model):
    user = models.ForeignKey(User, verbose_name='Foydalanuvchi', on_delete=models.CASCADE(), blank=True)

    name = models.CharField(verbose_name='ismi', max_length=100)
    email = models.EmailField(verbose_name='email')
    subject = models.CharField(verbose_name='mavzu', max_length=200)
    message = models.TextField(verbose_name='Murojaat', max_length=2000)


class AboutUs(models.Model):
    title = models.CharField(verbose_name='Sarlavha', max_length=400)
    text = models.TextField(verbose_name='haqimizda qisqacha')
    image = models.ImageField(verbose_name='Rasmi', upload_to='Media/About/images/', blank=True)
    teamwork = models.CharField(verbose_name='Jamoaviy ish', max_length=500)
    our_core_value = models.CharField(verbose_name='Bizning asosiy qadriyatimiz', max_length=1000)
    background = models.CharField(verbose_name='Ortki ishlar', max_length=500)
    telegram_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)



from django.db import models
from django.urls import reverse

from account.models import User


class Category(models.Model):
    name = models.CharField(verbose_name='Kategoriya', max_length=150)
    desc = models.TextField(verbose_name='Nima haqida')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Avtor', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, verbose_name='Kategoriyasi', on_delete=models.SET_NULL, null=True)

    title = models.CharField(verbose_name='Sarlavha', max_length=250)
    text = models.TextField(verbose_name='Post mazmuni')
    image = models.ImageField(verbose_name='Rasmi', upload_to='Media/Post/images/')
    date_created = models.DateField(verbose_name='Yaratilgan sana', auto_now_add=True)
    date_update = models.DateField(verbose_name='Yangilangan sana', auto_now=True)
    video = models.FileField(verbose_name='Video', blank=True, upload_to='Media/Post/videos/')

    url = models.SlugField(max_length=250, unique=True)
    active = models.BooleanField(verbose_name='Chop etilsin', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Avtor', on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, verbose_name='Post', related_name='comments', on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey('self', verbose_name='Vorisi', on_delete=models.SET_NULL, blank=True, null=True)

    text = models.CharField(verbose_name='Koment', max_length=500)
    date = models.DateTimeField(verbose_name='Sana vaqti', auto_now_add=True)

    def __str__(self):
        return str(self.author)

    def set(self):
        return reverse('post_detail', kwargs={'pk': id})

    class Meta:
        verbose_name = 'Komment'
        verbose_name_plural = 'Kommentlar'

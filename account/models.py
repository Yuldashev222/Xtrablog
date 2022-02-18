from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(verbose_name='Avatarka', upload_to='Media/User/avatars/', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Foydalanuvch'
        verbose_name_plural = 'Foydalanuvchilar'


class Employee(models.Model):
    user = models.ForeignKey(User, verbose_name='Xodim', on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(verbose_name='ismi', max_length=100)
    info = models.TextField(verbose_name='bio', blank=True)
    position = models.CharField(verbose_name='Lavozimi', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'

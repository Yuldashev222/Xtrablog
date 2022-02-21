# Generated by Django 4.0.2 on 2022-02-21 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Sarlavha')),
                ('text', models.TextField(verbose_name='haqimizda qisqacha')),
                ('image', models.ImageField(blank=True, upload_to='Media/About/images/', verbose_name='Rasmi')),
                ('teamwork', models.CharField(max_length=500, verbose_name='Jamoaviy ish')),
                ('our_core_value', models.CharField(max_length=1000, verbose_name='Bizning asosiy qadriyatimiz')),
                ('background', models.CharField(max_length=500, verbose_name='Ortki ishlar')),
                ('telegram_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('youtube_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ismi')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=200, verbose_name='mavzu')),
                ('message', models.TextField(max_length=2000, verbose_name='Murojaat')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
        ),
    ]
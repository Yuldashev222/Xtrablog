from django.urls import path
from .views import *
from post.views import *
from account.views import *

urlpatterns = [
    path('', posts, name='posts'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('post/', PostView.as_view(), name='post'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', filter_posts, name='filter_in_category_posts'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', log_out, name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
]

from django.urls import path
from .views import *
from post.views import *

urlpatterns = [
    path('', PostsView.as_view(), name='posts'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('post/', PostView.as_view(), name='post'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]

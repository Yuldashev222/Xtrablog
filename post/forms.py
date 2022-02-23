from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """ Komment forma """

    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):
    """ Post forma """

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'video', 'url', 'active', 'category']
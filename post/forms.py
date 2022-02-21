from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """ Komment forma """

    class Meta:
        model = Comment
        fields = ('text',)



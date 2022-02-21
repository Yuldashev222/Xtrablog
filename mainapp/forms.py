from django import forms

from .models import Messages


class MessagesForm(forms.ModelForm):
    """ Savol va takliflar formasi """

    class Meta:
        model = Messages
        fields = ('user', 'name', 'email', 'subject')

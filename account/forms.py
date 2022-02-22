from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegistrationForm(UserCreationForm):
    """ User registration formasi """

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')

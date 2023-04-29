from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegistrForm(UserCreationForm):
    email = forms.EmailField()
    number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ["username", "email", "number", "password1", "password2"]
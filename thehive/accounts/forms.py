from django import forms
from .models import UserProfile


class SupplierForm(forms.ModelForm):
    is_supplier = forms.BooleanField(required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'number', 'is_supplier']
# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['number']

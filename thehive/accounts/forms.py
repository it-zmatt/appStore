from django import forms
from .models import UserProfile


class SupplierForm(forms.ModelForm):
    is_supplier = forms.BooleanField(required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'number', 'is_supplier']
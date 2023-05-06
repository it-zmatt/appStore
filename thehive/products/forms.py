from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'unit_price', 'description','quantity', 'photo')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)







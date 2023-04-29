from django.shortcuts import render, redirect
from .forms import RegistrForm

# Create your views here.
def home(response):
    return render(response, 'registration/base.html')

def register(response):
    if response.method == 'POST':
        form = RegistrForm(response.POST)
        if form.is_valid():
            form.save()
                
    else:
         form = RegistrForm()
    return render(response, 'registration/index.html', {'form': form})


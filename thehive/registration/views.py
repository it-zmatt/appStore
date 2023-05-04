from django.conf import settings
from django.shortcuts import render, redirect
from .forms import RegistrForm
from django.contrib.auth.views import LoginView


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = settings.LOGIN_REDIRECT_URL

def home(response):
    return render(response, 'registration/base.html')

def register(response):
    if response.method == 'POST':
        form = RegistrForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('Login')          
    else:
         form = RegistrForm()
    return render(response, 'registration/index.html', {'form': form})


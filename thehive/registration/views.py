from django.conf import settings
from django.shortcuts import render, redirect
from .forms import RegistrForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User



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
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'This username is already taken.')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already taken.')
            else:
                form.save()
                return redirect('login')

    else:
         form = RegistrForm()
    return render(response, 'registration/index.html', {'form': form})


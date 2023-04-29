from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, 'registration/base.html')

def register(response):
    return render(response, 'registration/index.html')


from django.shortcuts import render

# Create your views here.
def profile(response):
    return render(response, 'accounts/base.html')

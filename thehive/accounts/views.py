from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect



# Create your views here.
@login_required
def profile(request):
    return render(request, 'accounts/base.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
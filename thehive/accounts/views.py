from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect
from .forms import SupplierForm
from supplier.models import Supplier
from django.db import IntegrityError
from django.db import transaction


# Create your views here.
@login_required
def profile(request):
    is_supplier = hasattr(request.user.profile, 'supplier')
    return render(request, 'accounts/base.html', {'user': request.user, 'is_supplier': is_supplier})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

@transaction.atomic
@login_required
def become_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            user_profile = request.user.profile
            user_profile.is_supplier = True
            user_profile.first_name = form.cleaned_data['first_name']
            user_profile.last_name = form.cleaned_data['last_name']
            user_profile.number = form.cleaned_data['number']
            user_profile.save()
            if user_profile.is_supplier:
                try:
                    supplier = Supplier.objects.create(user_profile=user_profile)
                except IntegrityError:
                    # If a supplier with the same user profile already exists, do nothing
                    pass
            return redirect('Profile')
    else:
        form = SupplierForm()
    return render(request, 'accounts/supplier.html', {'form': form})


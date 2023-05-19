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
from products.models import Order


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

def choice(request):
    return render(request, 'accounts/choice.html')

@login_required
def my_orders(request):
    orders = Order.objects.filter(customer=request.user)
    context = {'orders': orders}
    return render(request, 'accounts/my_orders.html', context)



from django.contrib import messages
from django.shortcuts import render, redirect

@login_required
def update_profile(request):
    if request.method == 'POST':
        # Get the updated values from the form
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')

        # Update the user's profile
        user = request.user
        user.username = new_username
        user.email = new_email
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.save()

        # Add a success message
        messages.success(request, 'Account information updated successfully.')

        # Redirect the user to the settings page or any other desired page
        return redirect('settings')

    # If the request method is not POST, render the empty form
    return render(request, 'accounts/update.html')

from django.contrib.auth import update_session_auth_hash


@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        user = request.user

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('change_password')
        else:
            messages.error(request, 'Invalid old password.')
            return redirect('change_password')

    return render(request, 'accounts/password.html')





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product, Order
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

@login_required
def order_list(request):
    if request.user.is_authenticated:
        supplier = request.user.profile.supplier
        products = Product.objects.filter(supplier=supplier)
        orders = Order.objects.filter(product__in=products)
        return render(request, 'supplier/order_list.html', {'orders': orders})
    else:
        return redirect('login')
    
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from products.models import Order

@login_required
def mark_as_sent(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.is_sent = True
    order.save()
    messages.success(request, 'Order marked as sent.')
    return redirect('Orders')

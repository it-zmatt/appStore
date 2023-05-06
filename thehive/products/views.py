from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm, SearchForm
from .models import Product



# Create your views here.
@login_required
def product_list(request):
    if request.user.is_authenticated:
        supplier = request.user.profile.supplier
        products = Product.objects.filter(supplier=supplier)
        return render(request, 'products/products_list.html', {'products': products})
    else:
        return redirect('login')


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            user_profile = request.user.profile
            product.supplier = user_profile.supplier
            product.save()
            messages.success(request, 'Product added successfully.')
            return redirect('Products')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form})

from django.shortcuts import render
from products.models import Product

def search(request):
    form = SearchForm(request.GET)
    results = None
    
    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        results = Product.objects.filter(name__icontains=search_query)
    
    return render(request, 'products/search_results.html', {'form': form, 'results': results})
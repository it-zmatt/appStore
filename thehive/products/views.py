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
            return redirect('Products')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form})


from django.shortcuts import render
from products.models import Product

@login_required
def search(request):
    form = SearchForm(request.GET)
    results = None
    
    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        results = Product.objects.filter(name__icontains=search_query)
    
    return render(request, 'products/search_results.html', {'form': form, 'results': results})

@login_required
def search_redirect(request):
    return redirect('search')

@login_required
def product_info(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'products/product_info.html', {'product': product})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Order

@login_required
def create_order(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        location = request.POST.get('location', '')
        address = request.POST.get('address', '')

        if quantity < product.quantity:
            messages.error(request, f'Please enter a quantity greater than or equal to {product.quantity}.')
        else:
            order = Order.objects.create(
                product=product,
                customer=request.user,
                supplier=product.supplier,
                quantity=quantity,
                location=location,
            )
            print(order)  # print the order object to verify that it's created successfully


            # Redirect to the order confirmation page
            return redirect('MyOrders')

    context = {'product': product}
    return render(request, 'products/create_order.html', context)

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

@require_POST
def confirm_received(request, pk):
    order = get_object_or_404(Order, pk=pk, customer=request.user)

    if order.is_sent:
        order.is_completed = True
        order.save()
    

    return redirect('MyOrders')


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('Products')
from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='Products'),
    path('add/', views.add_product, name='Add'),
    path('products/<int:product_id>/edit/', views.edit_product, name='Edit'),
    path('search/', views.search, name='search'),



]
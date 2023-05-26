from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='Products'),
    path('add/', views.add_product, name='Add'),
    path('products/<int:product_id>/edit/', views.edit_product, name='Edit'),
    path('search/', views.search, name='search'),
    path('search-redirect/', views.search_redirect, name='search_redirect'),
    path('/<int:product_id>/info/', views.product_info, name='Info'),
    path('create_order/<int:pk>/', views.create_order, name='create_order'),
    path('/<int:pk>/confirm_received/', views.confirm_received, name='confirm_received'),
    path('delete/<int:product_id>/', views.delete_product, name='Delete'),
]
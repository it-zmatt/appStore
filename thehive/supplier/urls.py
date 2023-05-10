from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('orders/', views.order_list, name='Orders'),
    path('orders/<int:order_id>/mark_as_sent/', views.mark_as_sent, name='mark_as_sent'),
]

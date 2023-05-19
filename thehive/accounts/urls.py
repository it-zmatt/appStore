from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.profile, name= 'Profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='Login'),
    path('logout/', views.logout_view, name='logout'),
    path('become_supplier/', views.become_supplier, name='become_supplier'),
    path('myOrders/', views.my_orders, name = 'MyOrders'),
    path('choice/', views.choice, name = 'choice'),
    path('settings/', views.update_profile, name='settings'),
    path('change_password/', views.change_password, name='change_password'),

]


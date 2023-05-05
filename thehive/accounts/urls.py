from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.profile, name= 'Profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='Login'),
    path('logout/', views.logout_view, name='logout'),
    path('become_supplier/', views.become_supplier, name='become_supplier'),
]


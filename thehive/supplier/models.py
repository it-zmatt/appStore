from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your models here.
class Supplier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
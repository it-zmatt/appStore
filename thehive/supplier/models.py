from django.db import models
from accounts.models import UserProfile

# Create your models here.


class Supplier(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='supplier', null=True, blank=True)

    def __str__(self):
        return str(self.user_profile)
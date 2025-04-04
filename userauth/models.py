from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class AdminUser(CustomUser):
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.username
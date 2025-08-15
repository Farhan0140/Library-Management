from django.db import models

from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class User( AbstractUser ):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Member( models.Model ):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


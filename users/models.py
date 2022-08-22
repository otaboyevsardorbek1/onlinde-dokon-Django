from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    city = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Import Custom KeyGen Library
from .keygen import userKEY

class Profile(AbstractUser):
    address = models.TextField(max_length=500, blank=True, default='Not Supplied')
    city = models.CharField(max_length=40, blank=True, default='Not Supplied')
    state = models.CharField(max_length=5, blank=True, default='NA')
    zipcode = models.CharField(max_length=12, blank=True, default='NA')
    userkey = models.CharField(max_length=20, default=userKEY, unique=True)
    pass

    def __str__(self):
        return self.username

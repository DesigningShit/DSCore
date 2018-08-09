from django.db import models as m
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Import Custom KeyGen Library
from .keygen import getRandomID

class Profile(AbstractUser):
    address = m.TextField(max_length=500, blank=True, default='Not Supplied')
    city = m.CharField(max_length=40, blank=True, default='Not Supplied')
    state = m.CharField(max_length=5, blank=True, default='NA')
    zipcode = m.CharField(max_length=12, blank=True, default='NA')
    userkey = m.CharField(max_length=20, default=getRandomID, unique=True)
    pass

    def __str__(self):
        return self.username
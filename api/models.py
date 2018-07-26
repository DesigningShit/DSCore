from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Import Custom KeyGen Library
from .keygen import userKEY, deviceID

class Profile(AbstractUser):
    address = models.TextField(max_length=500, blank=True, default='Not Supplied')
    city = models.CharField(max_length=40, blank=True, default='Not Supplied')
    state = models.CharField(max_length=5, blank=True, default='NA')
    zipcode = models.CharField(max_length=12, blank=True, default='NA')
    userkey = models.CharField(max_length=20, default=deviceID)

    def __str__(self):
        return self.username

class RouteKeeperDeviceModel(models.Model):
    owner = models.ForeignKey('Profile', related_name='owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='.')
    deviceid = models.CharField(max_length=25, default=deviceID)
    ipDeviceName = models.CharField(max_length=64, default='eth0')
    ipAddress = models.GenericIPAddressField(default='0.0.0.0')
    ipMask = models.GenericIPAddressField(default='0.0.0.0')
    ipGateway = models.GenericIPAddressField(default='0.0.0.0')
    ipExternalAddress = models.GenericIPAddressField(default='0.0.0.0')

    def __str__(self):
        return self.owner.username+' , '+self.deviceid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Import Custom KeyGen Library
from .keygen import userKEY, deviceID, channelID, sensorID

class Profile(AbstractUser):
    address = models.TextField(max_length=500, blank=True, default='Not Supplied')
    city = models.CharField(max_length=40, blank=True, default='Not Supplied')
    state = models.CharField(max_length=5, blank=True, default='NA')
    zipcode = models.CharField(max_length=12, blank=True, default='NA')
    userkey = models.CharField(max_length=20, default=deviceID, unique=True)
    pass

    def __str__(self):
        return self.username

class RouteKeeperDeviceModel(models.Model):
    owner = models.ForeignKey('Profile', related_name='owner', to_field='userkey', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='.')
    deviceid = models.CharField(max_length=25, default=deviceID, unique=True)
    ipDeviceName = models.CharField(max_length=64, default='eth0')
    ipAddress = models.GenericIPAddressField(default='0.0.0.0')
    ipMask = models.GenericIPAddressField(default='0.0.0.0')
    ipGateway = models.GenericIPAddressField(default='0.0.0.0')
    ipExternalAddress = models.GenericIPAddressField(default='0.0.0.0')
    pass

    def __str__(self):
        return self.owner.username+' , '+self.deviceid

class RouteKeeperDeviceHistoryModel(models.Model):
    deviceid = models.ForeignKey('RouteKeeperDeviceModel', to_field='deviceid', on_delete=models.CASCADE)
    statuscode = models.CharField(max_length=250, default='0000')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.deviceid.owner.username

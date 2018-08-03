from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Import Custom KeyGen Library
from api.keygen import userKEY, deviceID, channelID, sensorID

#Import the Profile
from api.models import Profile

class RouteKeeperDeviceModel(models.Model):
    owner = models.ForeignKey('api.Profile', related_name='owner', to_field='userkey', on_delete=models.CASCADE, help_text='Userkey of the device owner (ex. g215c-q955g)')
    name = models.CharField(max_length=250, default='.', help_text='Name of the device (ex. RouteKeeper at House.)')
    deviceid = models.CharField(max_length=25, default=deviceID, unique=True, help_text='DeviceKEY for the device')
    ipDeviceName = models.CharField(max_length=64, default='eth0', help_text='Name of the device interface (ex. wlan0, en0, eth0, etc)')
    ipAddress = models.GenericIPAddressField(default='0.0.0.0', help_text='IP Address of the device interface (ex. 192.168.1.2)')
    ipMask = models.GenericIPAddressField(default='0.0.0.0', help_text='Subnet Mask Address of the device interface (ex. 255.255.255.0)')
    ipGateway = models.GenericIPAddressField(default='0.0.0.0', help_text='Default Gateway Address of the device interface (ex. 192.168.1.1)')
    ipExternalAddress = models.GenericIPAddressField(default='0.0.0.0', help_text='External Address of the device interface (ex. 64.181.10.22)')
    pass

    def __str__(self):
        return self.owner.username+' , '+self.deviceid

class RouteKeeperDeviceHistoryModel(models.Model):
    deviceid = models.ForeignKey('RouteKeeperDeviceModel', to_field='deviceid', on_delete=models.CASCADE)
    statuscode = models.CharField(max_length=250, default='0000')
    datetime = models.DateTimeField(auto_now_add=True)
    pass
    
    def __str__(self):
        return self.deviceid.owner.username

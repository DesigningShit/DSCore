from django.db import models
from api.keygen import channelID, sensorID, dataID, getRandomID
from api.models import Profile

class IOTTenant(models.Model):
    owner = models.ForeignKey('api.Profile', related_name='TenantOwner', to_field='userkey', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default='.')
    tenantid = models.CharField(max_length=30, default=getRandomID, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class IOTCustomer(models.Model):
    owner = models.ForeignKey('IOTTenant', related_name='TenantOwner', to_field='tenantid', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default='.')
    customerid = models.CharField(max_length=30, default=getRandomID, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class IOTChannelModel(models.Model):
    channelowner = models.ForeignKey('IOTCustomer', related_name='channelowner', to_field='customerid', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='.')
    channelid = models.CharField(max_length=30, default=channelID, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class IOTSensorModel(models.Model):
    channel = models.ForeignKey('IOTChannelModel', related_name='channel', to_field='channelid', on_delete=models.CASCADE)
    sensorid = models.CharField(max_length=30, default=sensorID, unique=True)
    name = models.CharField(max_length=250, default='Not Supplied')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    context = models.CharField(max_length=250, default='Undefined')

    def __str__(self):
        return self.name

class IOTSensorReadingModel(models.Model):
    sensor = models.ForeignKey('IOTSensorModel', related_name='sensor', to_field='sensorid', on_delete=models.CASCADE)
    readingid = models.CharField(max_length=30, default=dataID, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    data = models.CharField(max_length=250, default='Not Supplied')

    def __str__(self):
        return self.sensor.sensorid+':'+self.data
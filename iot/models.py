from django.db import models as m
from api.keygen import getRandomID
from api.models import Profile

class IOTTenant(m.Model):
    owner = m.ForeignKey('api.Profile', related_name='TenantOwner', to_field='userkey', on_delete=m.CASCADE)
    name = m.CharField(max_length=150, default='.')
    tenantid = m.CharField(max_length=30, default=getRandomID, unique=True)
    created = m.DateTimeField(auto_now_add=True)
    modified = m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class IOTCustomer(m.Model):
    owner = m.ForeignKey('IOTTenant', related_name='TenantOwner', to_field='tenantid', on_delete=m.CASCADE)
    name = m.CharField(max_length=150, default='.')
    customerid = m.CharField(max_length=30, default=getRandomID, unique=True)
    created = m.DateTimeField(auto_now_add=True)
    modified = m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class IOTChannelModel(m.Model):
    channelowner = m.ForeignKey('IOTCustomer', related_name='channelowner', to_field='customerid', on_delete=m.CASCADE)
    name = m.CharField(max_length=250, default='.')
    channelid = m.CharField(max_length=30, default=getRandomID, unique=True)
    created = m.DateTimeField(auto_now_add=True)
    modified = m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class IOTSensorModel(m.Model):
    channel = m.ForeignKey('IOTChannelModel', related_name='channel', to_field='channelid', on_delete=m.CASCADE)
    sensorid = m.CharField(max_length=30, default=getRandomID, unique=True)
    name = m.CharField(max_length=250, default='Not Supplied')
    created = m.DateTimeField(auto_now_add=True)
    modified = m.DateTimeField(auto_now=True)
    context = m.CharField(max_length=250, default='Undefined')

    def __str__(self):
        return self.name

class IOTSensorReadingModel(m.Model):
    sensor = m.ForeignKey('IOTSensorModel', related_name='sensor', to_field='sensorid', on_delete=m.CASCADE)
    readingid = m.CharField(max_length=30, default=getRandomID, unique=True)
    created = m.DateTimeField(auto_now_add=True)
    modified = m.DateTimeField(auto_now=True)
    data = m.CharField(max_length=250, default='Not Supplied')

    def __str__(self):
        return self.sensor.sensorid+':'+self.data
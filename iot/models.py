from django.db import models
from api.keygen import userKEY, deviceID, channelID, sensorID
from api.models import Profile

class IOTChannelModel(models.Model):
    channelowner = models.ForeignKey('api.Profile', related_name='channelowner', to_field='userkey', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='.')
    channelid = models.CharField(max_length=30, default=channelID, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class IOTSensorModel(models.Model):
    channel = models.ForeignKey('IOTChannelModel', related_name='channel', to_field='channelid', on_delete=models.CASCADE)
    sensorid = models.CharField(max_length=30, default=sensorID, unique=True)
    name = models.CharField(max_length=250, default='Not Supplied')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class IOTSensorReadingModel(models.Model):
    sensor = models.ForeignKey('IOTSensorModel', related_name='sensor', to_field='sensorid', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    data = models.CharField(max_length=250, default='Not Supplied')

    def __str__(self):
        return self.sensor.name+':'+self.data
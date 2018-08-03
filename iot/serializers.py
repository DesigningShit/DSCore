from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import filters
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel
import api.serializers


# Serializers are Here
class IOTChannelModelSerializer(serializers.ModelSerializer):
    """
    IOT Channel Serializer
    """
    class Meta:
        model = IOTChannelModel
        fields = ('name','channelowner','channelid','created')
        read_only_fields = ('channelid','created')

class IOTSensorModelSerializer(serializers.ModelSerializer):
    """
    IOT Sensor Serializer
    """
    channel = IOTChannelModel.objects.all()
    owner = serializers.CharField(source='sensor.channel.channelowner.userkey',read_only=True)
    
    class Meta:
        model = IOTSensorModel
        fields = ('name' , 'sensorid' , 'channel' , 'created' , 'owner' , 'context')
        read_only_fields = ('sensorid' , 'created' , 'owner')

class IOTSensorReadingModelSerializer(serializers.ModelSerializer):
    """
    IOT Sensor Data Serializer
    """
    sensor = IOTSensorModelSerializer()
    owner = serializers.CharField(source='sensor.channel.channelowner.userkey',read_only=True)

    class Meta:
        model = IOTSensorReadingModel
        fields = ('readingid' , 'created' , 'data' , 'sensor' , 'owner')
        read_only_fields = ('created' , 'channelid' , 'readingid')

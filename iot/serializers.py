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
    owner_firstname = serializers.CharField(source='channelowner.first_name',read_only=True)
    owner_lastname = serializers.CharField(source='channelowner.last_name',read_only=True)
    
    class Meta:
        model = IOTChannelModel
        fields = ('name','channelowner','owner_firstname','owner_lastname','channelid','created', 'modified')
        read_only_fields = ('channelid','created','modified','owner_firstname','owner_lastname')

class IOTSensorModelSerializer(serializers.ModelSerializer):
    """
    IOT Sensor Serializer
    """
    channel = IOTChannelModel.objects.all()
    owner = serializers.CharField(source='channel.channelowner.userkey',read_only=True)
    channelname = serializers.CharField(source='channel.name',read_only=True)

    class Meta:
        model = IOTSensorModel
        fields = ('name' , 'channel' ,'channelname','context' , 'sensorid' , 'owner' , 'created' , 'modified')
        read_only_fields = ('sensorid' , 'created' , 'owner', 'modified')

class IOTSensorReadingModelSerializer(serializers.ModelSerializer):
    """
    IOT Sensor Data Serializer
    """
    sensor = IOTSensorModel.objects.all()

    class Meta:
        model = IOTSensorReadingModel
        fields = ('sensor','readingid','data','created','modified')
        read_only_fields = ('created' , 'channelid' , 'readingid','modified','context')

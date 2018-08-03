from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import filters
from django.contrib.auth.models import User
from api.models import Profile
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel
# from drf_writable_nested import WritableNestedModelSerializer
import api.serializers


# Serializers are Here
class IOTChannelModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = IOTChannelModel
        fields = ('name','channelowner','channelid','created')
        read_only_fields = ('channelid','created')

class IOTSensorModelSerializer(serializers.ModelSerializer):
    channel = IOTChannelModel.objects.all()
    owner = serializers.CharField(source='sensor.channel.channelowner.userkey',read_only=True)
    
    class Meta:
        model = IOTSensorModel
        fields = ('name','sensorid','channel','created','owner')
        read_only_fields = ('sensorid','created','owner')

class IOTSensorReadingModelSerializer(serializers.ModelSerializer):
    sensor = IOTSensorModel.objects.all()
    sensorname = serializers.CharField(source='sensor.name',read_only=True)
    channel = serializers.CharField(source='sensor.channel.name',read_only=True)
    channelid = serializers.CharField(source='sensor.channel.channelid',read_only=True)
    owner = serializers.CharField(source='sensor.channel.channelowner.userkey',read_only=True)

    class Meta:
        model = IOTSensorReadingModel
        fields = ('created','data','sensor', 'sensorname', 'channel', 'channelid', 'owner')
        read_only_fields = ('sensorname','created','channel','channelid',)

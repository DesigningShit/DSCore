from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import filters
from django.contrib.auth.models import User
from api.models import Profile
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel
from drf_writable_nested import WritableNestedModelSerializer
import api.serializers


# Serializers are Here
class TestUserSerializer(serializers.ModelSerializer):
    """User Information Serializer"""

    class Meta:
        model = Profile
        fields = ('last_login','username','first_name','last_name','email','date_joined','address','city','state','zipcode','userkey')
        exclude_fields = ('url')
        read_only_fields = ('userkey',)

class ChannelInformationSerializer(serializers.ModelSerializer):
    """Channel Information Serializer."""

    class Meta:
        fields = ('channelowner', 'name', 'channelid', 'created')
        nested_proxy_field = True

class IOTChannelModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = IOTChannelModel
        fields = ('name','channelowner','channelid','created')
        read_only_fields = ('channelid','created')

class IOTSensorModelSerializer(serializers.ModelSerializer):
    channel = serializers.CharField(source='channel.channelid')
    owner = serializers.CharField(source='channel.channelowner.userkey', read_only=True)
    
    
    class Meta:
        model = IOTSensorModel
        fields = ('name','sensorid','channel','created','owner')
        read_only_fields = ('sensorid','created')


class IOTSensorReadingModelSerializer(serializers.ModelSerializer):
    sensor = serializers.CharField(source='sensor.sensorid')
    sensorname = serializers.CharField(source='sensor.name',read_only=True)
    channel = serializers.CharField(source='sensor.channel.name',read_only=True)
    channelid = serializers.CharField(source='sensor.channel.channelid',read_only=True)
    owner = serializers.CharField(source='sensor.channel.channelowner.userkey',read_only=True)

    class Meta:
        model = IOTSensorReadingModel
        fields = ('created','data','sensor', 'sensorname', 'channel', 'channelid', 'owner')
        read_only_fields = ('sensorname','created','channel','channelid',)

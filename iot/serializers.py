from rest_framework import viewsets
from rest_framework import serializers as s
from rest_framework import filters
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel, IOTTenant, IOTCustomer
# import api.serializers


# Serializers are Here
class IOTTenantModelSerializer(s.ModelSerializer):
    """
    IOT Sensor Data Serializer
    """
    sensor = IOTTenant.objects.all()

    class Meta:
        model = IOTTenant
        fields = ('owner', 'name', 'tenantid', 'created', 'modified')
        read_only_fields = ('tenantid' , 'modified' , 'created')

class IOTCustomerModelSerializer(s.ModelSerializer):
    """
    IOT Sensor Data Serializer
    """
    sensor = IOTCustomer.objects.all()

    class Meta:
        model = IOTCustomer
        fields = ('name','customerid','owner','created','modified')
        read_only_fields = ('customerid' , 'modified' , 'created')

class IOTChannelModelSerializer(s.ModelSerializer):
    """
    IOT Channel Serializer
    """
    class Meta:
        model = IOTChannelModel
        fields = ('name','channelowner','channelid','created', 'modified')
        read_only_fields = ('channelid','created','modified','owner_firstname','owner_lastname')

class IOTSensorModelSerializer(s.ModelSerializer):
    """
    IOT Sensor Serializer
    """
    class Meta:
        model = IOTSensorModel
        fields = ('sensorid' , 'name' , 'sensorid' , 'context' , 'channel' , 'created' , 'modified')
        read_only_fields = ('sensorid' , 'created' , 'modified')

class IOTSensorReadingModelSerializer(s.ModelSerializer):
    """
    IOT Sensor Data Serializer
    """
    sensor = IOTSensorModel.objects.all()

    class Meta:
        model = IOTSensorReadingModel
        fields = ('sensor','readingid','data','created','modified')
        read_only_fields = ('created' , 'channelid' , 'readingid','modified','context')

from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import filters
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel

# Serializers are Here
class IOTChannelModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = IOTChannelModel
        fields = ('name','channelowner','channelid','created')
        read_only_fields = ('channelid','created')

class IOTSensorModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IOTSensorModel
        fields = ('name','sensorid','channel','created')
        read_only_fields = ('sensorid','created')

class IOTSensorReadingModelSerializer(serializers.ModelSerializer):
    sensor = serializers.CharField(source='sensor.sensorid')
    sensorname = serializers.CharField(source='sensor.name',read_only=True)
    channel = serializers.CharField(source='sensor.channel.name',read_only=True)
    channelid = serializers.CharField(source='sensor.channel.channelid',read_only=True)

    class Meta:
        model = IOTSensorReadingModel
        fields = ('created','data','sensor', 'sensorname', 'channel', 'channelid',)
        read_only_fields = ('sensorname','created','channel','channelid',)

# Views/Viewsets are Here
class IOTChannelModelViewSet(viewsets.ModelViewSet):
    queryset = IOTChannelModel.objects.all()
    serializer_class = IOTChannelModelSerializer

class IOTSensorModelViewSet(viewsets.ModelViewSet):
    queryset = IOTSensorModel.objects.all()
    serializer_class = IOTSensorModelSerializer

class IOTSensorReadingModelViewSet(viewsets.ModelViewSet):
    queryset = IOTSensorReadingModel.objects.all()
    serializer_class = IOTSensorReadingModelSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('sensor__name', 'sensor__sensorid', 'data', 'sensor__channel__name', 'sensor__channel__channelid' )
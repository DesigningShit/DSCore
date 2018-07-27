from rest_framework import viewsets
from rest_framework import serializers
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel

# Serializers are Here
class IOTChannelModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = IOTChannelModel
        fields = ('name','channelowner','channelid','created')
        exclude_fields = ('id',)

class IOTSensorModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IOTSensorModel
        fields = ('name','sensorid','channel','created')
        exclude_fields = ('id',)
        # depth = 1

class IOTSensorReadingModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IOTSensorReadingModel
        fields = ('created','data','sensor',)
        exclude_fields = ('id',)
        # depth = 2

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


from rest_framework import viewsets
from rest_framework import filters
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel
from .serializers import IOTChannelModelSerializer, IOTSensorModelSerializer, IOTSensorReadingModelSerializer

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
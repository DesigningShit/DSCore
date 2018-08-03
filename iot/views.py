from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, status, permissions, filters
from rest_framework.decorators import api_view, renderer_classes, permission_classes, list_route
from api.models import Profile
from api.serializers import UserProfileSerializer, UserProfileURLSerializer
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel
from .serializers import IOTChannelModelSerializer, IOTSensorModelSerializer, IOTSensorReadingModelSerializer

# Views/Viewsets are Here
class IOTChannelModelViewSet(viewsets.ModelViewSet):
    """
    Channel view allows the user to query the API for a list or individual channel, as well as make updates or deletions.
    """
    queryset = IOTChannelModel.objects.all()
    serializer_class = IOTChannelModelSerializer
    lookup_field = "channelid"

    def get_queryset(self):
            """
            This view should return a list of all the IOT Channels
            for the currently authenticated user.
            """
            user = self.request.user
            if user.is_superuser:
                return IOTChannelModel.objects.all()
            else:
                return IOTChannelModel.objects.filter(channelowner=user)

class IOTSensorModelViewSet(viewsets.ModelViewSet):
    """
    Sensor ViewSet
    """
    queryset = IOTSensorModel.objects.all()
    serializer_class = IOTSensorModelSerializer
    lookup_field = "sensorid"

    def get_queryset(self):
            """
            This view should return a list of all the IOT Sensors
            for the currently authenticated user.
            """
            user = self.request.user
            if user.is_superuser:
                return IOTSensorModel.objects.all()
            else:
                return IOTSensorModel.objects.filter(channel__channelowner=user)


class IOTSensorReadingModelViewSet(viewsets.ModelViewSet):
    """
    Sensor Reading ViewSet
    """
    queryset = IOTSensorReadingModel.objects.all()
    serializer_class = IOTSensorReadingModelSerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = "readingid"
    search_fields = ('readingid','sensor__name', 'sensor__sensorid', 'data', 'sensor__channel__name', 'sensor__channel__channelid','sensor__context' )

    def get_queryset(self):
            """
            This view should return a list of all the 
            IOT Sensor Reading for the currently authenticated user.
            """
            user = self.request.user
            if user.is_superuser:
                return IOTSensorReadingModel.objects.all()
            else:
                return IOTSensorReadingModel.objects.filter(sensor__channel__channelowner=user)
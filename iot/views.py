from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, status, permissions, filters
from rest_framework.decorators import api_view, renderer_classes, permission_classes, list_route
from api.models import Profile
from api.serializers import UserProfileSerializer, UserProfileURLSerializer
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel, IOTTenant, IOTCustomer
from .serializers import IOTChannelModelSerializer, IOTSensorModelSerializer, IOTSensorReadingModelSerializer, IOTTenantModelSerializer, IOTCustomerModelSerializer

# Views/Viewsets are Here
class IOTTenantModelViewSet(viewsets.ModelViewSet):
    queryset = IOTTenant.objects.all()
    serializer_class = IOTTenantModelSerializer
    lookup_field = "tenantid"

    def get_queryset(self):
            user = self.request.user
            if user.is_superuser:
                return IOTTenant.objects.all()
            else:
                return IOTTenant.objects.filter(owner=user)

class IOTCustomerModelViewSet(viewsets.ModelViewSet):
    queryset = IOTCustomer.objects.all()
    serializer_class = IOTCustomerModelSerializer
    lookup_field = "customerid"

    def get_queryset(self):
            user = self.request.user
            if user.is_superuser:
                return IOTCustomer.objects.all()
            else:
                return IOTCustomer.objects.filter(owner__owner=user)

class IOTChannelModelViewSet(viewsets.ModelViewSet):
    queryset = IOTChannelModel.objects.all()
    serializer_class = IOTChannelModelSerializer
    lookup_field = "channelid"

    def get_queryset(self):
            user = self.request.user
            if user.is_superuser:
                return IOTChannelModel.objects.all()
            else:
                return IOTChannelModel.objects.filter(channelowner__owner__owner=user)

class IOTSensorModelViewSet(viewsets.ModelViewSet):
    queryset = IOTSensorModel.objects.all()
    serializer_class = IOTSensorModelSerializer
    lookup_field = "sensorid"

    def get_queryset(self):
            user = self.request.user
            if user.is_superuser:
                return IOTSensorModel.objects.all()
            else:
                return IOTSensorModel.objects.filter(channel__channelowner__owner__owner=user)


class IOTSensorReadingModelViewSet(viewsets.ModelViewSet):
    queryset = IOTSensorReadingModel.objects.all()
    serializer_class = IOTSensorReadingModelSerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = "readingid"
    search_fields = ('readingid','sensor__name', 'sensor__sensorid', 'data', 'sensor__channel__name', 'sensor__channel__channelid','sensor__context' )

    def get_queryset(self):
            user = self.request.user
            if user.is_superuser:
                return IOTSensorReadingModel.objects.all()
            else:
                return IOTSensorReadingModel.objects.filter(sensor__channel__channelowner__owner__owner=user)
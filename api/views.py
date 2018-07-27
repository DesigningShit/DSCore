from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import api_view, renderer_classes, permission_classes, list_route
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .models import RouteKeeperDeviceModel, Profile, RouteKeeperDeviceHistoryModel
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel
from .serializers import RouteKeeperDeviceModelSerializer, UserProfileSerializer, UserProfileURLSerializer, RouteKeeperDeviceHistoryModelSerializer
from .serializers import IOTChannelModelSerializer, IOTSensorModelSerializer, IOTSensorReadingModelSerializer
from .keys import GEO_ACCESS_KEY, WEATHER_APP_ID

class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileURLSerializer

    @list_route(methods=['get'], url_path='username/(?P<username>\w+)')
    def getByUsername(self, request, username ):
        user = get_object_or_404(Profile, username=username)
        return Response(UserProfileSerializer(user).data, status=status.HTTP_200_OK)

class RouteKeeperDeviceModelViewSet(viewsets.ModelViewSet):
    queryset = RouteKeeperDeviceModel.objects.all()
    serializer_class = RouteKeeperDeviceModelSerializer

class RouteKeeperDeviceHistoryModelViewSet(viewsets.ModelViewSet):
    queryset = RouteKeeperDeviceHistoryModel.objects.all()
    serializer_class = RouteKeeperDeviceHistoryModelSerializer

class IOTChannelModelViewSet(viewsets.ModelViewSet):
    queryset = IOTChannelModel.objects.all()
    serializer_class = IOTChannelModelSerializer

class IOTSensorModelViewSet(viewsets.ModelViewSet):
    queryset = IOTSensorModel.objects.all()
    serializer_class = IOTSensorModelSerializer

class IOTSensorReadingModelViewSet(viewsets.ModelViewSet):
    queryset = IOTSensorReadingModel.objects.all()
    serializer_class = IOTSensorReadingModelSerializer

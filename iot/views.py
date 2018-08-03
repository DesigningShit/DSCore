from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, status, permissions, filters
from rest_framework.decorators import api_view, renderer_classes, permission_classes, list_route
from api.models import Profile
from api.serializers import UserProfileSerializer, UserProfileURLSerializer
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel
from .serializers import IOTChannelModelSerializer, IOTSensorModelSerializer, IOTSensorReadingModelSerializer, TestUserSerializer

# Views/Viewsets are Here
class TestViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = TestUserSerializer

    @list_route(methods=['get'], url_path='username/(?P<username>\w+)')
    def getByUsername(self, request, username ):
        user = get_object_or_404(Profile, username=username)
        return Response(TestUserSerializer(user).data, status=status.HTTP_200_OK)

class IOTChannelModelViewSet(viewsets.ModelViewSet):
    queryset = IOTChannelModel.objects.all()
    serializer_class = IOTChannelModelSerializer

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
    queryset = IOTSensorModel.objects.all()
    serializer_class = IOTSensorModelSerializer

    def get_queryset(self):
            """
            This view should return a list of all the IOT Channels
            for the currently authenticated user.
            """
            user = self.request.user
            if user.is_superuser:
                return IOTSensorModel.objects.all()
            else:
                return IOTSensorModel.objects.filter(channel__channelowner=user)


class IOTSensorReadingModelViewSet(viewsets.ModelViewSet):
    queryset = IOTSensorReadingModel.objects.all()
    serializer_class = IOTSensorReadingModelSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('sensor__name', 'sensor__sensorid', 'data', 'sensor__channel__name', 'sensor__channel__channelid' )
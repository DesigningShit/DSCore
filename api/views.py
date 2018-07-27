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
from .serializers import RouteKeeperDeviceModelSerializer, UserProfileSerializer, UserProfileURLSerializer, RouteKeeperDeviceHistoryModelSerializer

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

    def get_queryset(self):
            """
            This view should return a list of all the RouteKeepers
            for the currently authenticated user.
            """
            user = self.request.user
            if user.is_superuser:
                return RouteKeeperDeviceModel.objects.all()
            else:
                return RouteKeeperDeviceModel.objects.filter(owner=user)

class RouteKeeperDeviceHistoryModelViewSet(viewsets.ModelViewSet):
    queryset = RouteKeeperDeviceHistoryModel.objects.all()
    serializer_class = RouteKeeperDeviceHistoryModelSerializer

    def get_queryset(self):
            """
            This view should return a list of all the RouteKeeper
            History for the currently authenticated user.
            """
            user = self.request.user
            if user.is_superuser:
                return RouteKeeperDeviceHistoryModel.objects.all()
            else:
                return RouteKeeperDeviceHistoryModel.objects.filter(deviceid__owner=user)
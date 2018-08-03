from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, status, permissions, filters
from rest_framework.decorators import api_view, renderer_classes, permission_classes, list_route
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .models import RouteKeeperDeviceHistoryModel, RouteKeeperDeviceModel
from .serializers import RouteKeeperDeviceModelSerializer, RouteKeeperDeviceHistoryModelSerializer

class RouteKeeperDeviceModelViewSet(viewsets.ModelViewSet):
    queryset = RouteKeeperDeviceModel.objects.all()
    serializer_class = RouteKeeperDeviceModelSerializer
    lookup_field = "deviceid"
    filter_backends = (filters.SearchFilter,)
    search_fields = ('deviceid','ipDeviceName', 'ipExternalAddress')

    def get_queryset(self):
            user = self.request.user
            if user.is_superuser:
                return RouteKeeperDeviceModel.objects.all()
            else:
                return RouteKeeperDeviceModel.objects.filter(owner=user)

class RouteKeeperDeviceHistoryModelViewSet(viewsets.ModelViewSet):
    queryset = RouteKeeperDeviceHistoryModel.objects.all()
    serializer_class = RouteKeeperDeviceHistoryModelSerializer
    lookup_field = "deviceid"
    filter_backends = (filters.SearchFilter,)
    search_fields = ('deviceid','statuscode', 'datetime')

    def get_queryset(self):
            user = self.request.user
            if user.is_superuser:
                return RouteKeeperDeviceHistoryModel.objects.all()
            else:
                return RouteKeeperDeviceHistoryModel.objects.filter(deviceid__owner=user)
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
from .models import RouteKeeperDeviceModel, Profile
from .serializers import RouteKeeperDeviceModelSerializer, UserProfileSerializer, UserProfileURLSerializer
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

@api_view(('GET','POST'))
@renderer_classes((BrowsableAPIRenderer, JSONRenderer,))
@permission_classes((permissions.AllowAny,))
def getlocationbyip(request):
    if request.data:
        ipaddress = str(request.data)
    else: 
        ipaddress='68.184.244.175'
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, )
    response = requests.get('http://api.ipstack.com/'+ipaddress+'?access_key='+GEO_ACCESS_KEY)
    geodata = response.json()
    if response:
        return Response(geodata, status=status.HTTP_200_OK)
    return Response(response, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET','POST'))
@renderer_classes((BrowsableAPIRenderer, JSONRenderer,))
@permission_classes((permissions.AllowAny,))
def getweather(request):
    if request.data:
        zipcode = str(request.data)
    else: 
        zipcode='63304'
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, )
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid='+WEATHER_APP_ID)
    weather = response.json()
    if weather:
        return Response(weather, status=status.HTTP_200_OK)
    return Response(response, status=status.HTTP_400_BAD_REQUEST)

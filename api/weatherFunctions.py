from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import api_view, renderer_classes, permission_classes, list_route
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .keys import WEATHER_APP_ID

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
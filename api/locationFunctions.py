from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import api_view, renderer_classes, permission_classes, list_route
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .keys import GEO_ACCESS_KEY

@api_view(('GET','POST'))
@renderer_classes((BrowsableAPIRenderer, JSONRenderer,))
@permission_classes((permissions.AllowAny,))
def getlocationbyip(request):
    if request.data:
        ipaddress = str(request.data)
    else: 
        return Response('IP Address Not Sent in Pipeline', status=status.HTTP_400_BAD_REQUEST)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, )
    response = requests.get('http://api.ipstack.com/'+ipaddress+'?access_key='+GEO_ACCESS_KEY)
    geodata = response.json()
    if response:
        return Response(geodata, status=status.HTTP_200_OK)
    return Response(response, status=status.HTTP_400_BAD_REQUEST)
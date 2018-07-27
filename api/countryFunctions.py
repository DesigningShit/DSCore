from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import api_view, renderer_classes, permission_classes, list_route
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

@api_view(('GET','POST'))
@renderer_classes((BrowsableAPIRenderer, JSONRenderer,))
@permission_classes((permissions.AllowAny,))
def getallcountries(request):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, )
    response = requests.get('https://restcountries.eu/rest/v2/all')
    geodata = response.json()
    if response:
        return Response(geodata, status=status.HTTP_200_OK)
    return Response(response, status=status.HTTP_400_BAD_REQUEST)
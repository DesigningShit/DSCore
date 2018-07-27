from django.urls import path, include
from .views import IOTChannelModelViewSet, IOTSensorModelViewSet, IOTSensorReadingModelViewSet


urlpatterns = [
    path(r'/channel', IOTChannelModelViewSet, name='IOT Channels'),
    path(r'/sensor', IOTSensorModelViewSet, name="IOT Sensors"),
    path(r'/sensordata', IOTSensorReadingModelViewSet, name='IOT Data'),
]


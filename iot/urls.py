from django.urls import path
from .views import IOTChannelModelViewSet, IOTSensorModelViewSet, IOTSensorReadingModelViewSet, TestViewSet

urlpatterns = [
    path(r'/channel', IOTChannelModelViewSet, name='IOT Channels'),
    path(r'/sensor', IOTSensorModelViewSet, name="IOT Sensors"),
    path(r'/sensordata', IOTSensorReadingModelViewSet, name='IOT Data'),
    path(r'/users', TestViewSet, name = 'TEST')
]


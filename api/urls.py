from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, RouteKeeperDeviceModelViewSet, RouteKeeperDeviceHistoryModelViewSet
from .locationFunctions import getlocationbyip
from .weatherFunctions import getweather
from .countryFunctions import getallcountries
from iot.views import IOTChannelModelViewSet, IOTSensorModelViewSet, IOTSensorReadingModelViewSet, TestViewSet
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

# REST loves routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rkdevices', RouteKeeperDeviceModelViewSet)
router.register(r'rkdevicehistory', RouteKeeperDeviceHistoryModelViewSet)
router.register(r'iot/channel', IOTChannelModelViewSet)
router.register(r'iot/sensor', IOTSensorModelViewSet)
router.register(r'iot/data', IOTSensorReadingModelViewSet)
router.register(r'iot/users', TestViewSet)

# Add the routers from above to the URL patterns
urlpatterns = [
    path(r'', include(router.urls)),
    #path(r'iot', include('iot.urls')),
    path(r'docs/', include_docs_urls(title='DS Core API')),
    path('weather/get/byzip', getweather, name='getweather'),
    path('location/get/byip', getlocationbyip, name='getlocationbyip'),
    path('location/get/countries', getallcountries, name='getcountrylist'),
]

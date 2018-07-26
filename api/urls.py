from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, RouteKeeperDeviceModelViewSet, getlocationbyip, getweather
from rest_framework import routers

# REST loves routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rkdevices', RouteKeeperDeviceModelViewSet)


# Add the routers from above to the URL patterns
urlpatterns = [
    path(r'', include(router.urls)),
    path('weather/get/byzip', getweather, name='getweather'),
    path('location/get/byip', getlocationbyip, name='getlocationbyip'),
]

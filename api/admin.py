from django.contrib import admin
from .models import RouteKeeperDeviceModel, Profile, RouteKeeperDeviceHistoryModel

# Registering our Custom Models Here
admin.site.register(RouteKeeperDeviceModel)
admin.site.register(RouteKeeperDeviceHistoryModel)
admin.site.register(Profile)

from django.contrib import admin
from .models import RouteKeeperDeviceModel, Profile, RouteKeeperDeviceHistoryModel, IOTChannelModel, IOTSensorModel, IOTSensorReadingModel

# Registering our Custom Models Here
admin.site.register(RouteKeeperDeviceModel)
admin.site.register(RouteKeeperDeviceHistoryModel)
admin.site.register(Profile)
admin.site.register(IOTChannelModel)
admin.site.register(IOTSensorModel)
admin.site.register(IOTSensorReadingModel)


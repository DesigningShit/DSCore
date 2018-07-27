from django.contrib import admin
from .models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel

# Registering our Custom Models Here
admin.site.register(IOTChannelModel)
admin.site.register(IOTSensorModel)
admin.site.register(IOTSensorReadingModel)


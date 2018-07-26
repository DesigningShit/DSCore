from django.contrib import admin
from .models import RouteKeeperDeviceModel, Profile

# Registering our Custom Models Here
admin.site.register(RouteKeeperDeviceModel)
admin.site.register(Profile)

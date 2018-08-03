from django.contrib import admin
from .models import RouteKeeperDeviceHistoryModel, RouteKeeperDeviceModel
from django.contrib.auth.admin import UserAdmin

admin.site.register(RouteKeeperDeviceModel)
admin.site.register(RouteKeeperDeviceHistoryModel)


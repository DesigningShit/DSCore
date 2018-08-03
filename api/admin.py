from django.contrib import admin
from .models import RouteKeeperDeviceModel, Profile, RouteKeeperDeviceHistoryModel
from django.contrib.auth.admin import UserAdmin

class ProfileAdmin(UserAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
# Registering our Custom Models Here
admin.site.register(RouteKeeperDeviceModel)
admin.site.register(RouteKeeperDeviceHistoryModel)


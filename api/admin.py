from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin

class ProfileAdmin(UserAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
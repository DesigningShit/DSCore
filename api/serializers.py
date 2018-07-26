from django.contrib.auth.models import User
from rest_framework import serializers
from .models import RouteKeeperDeviceModel, Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')
        exclude_fields = ('url')

class UserProfileURLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class RouteKeeperDeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteKeeperDeviceModel
        fields = ('__all__')
        read_only_fields = ('deviceid',)
        # fields = '__all__'

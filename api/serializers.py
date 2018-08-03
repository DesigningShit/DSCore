from django.contrib.auth.models import User
from rest_framework import serializers
from .models import RouteKeeperDeviceModel, Profile, RouteKeeperDeviceHistoryModel

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('last_login','username','first_name','last_name','email','date_joined','address','city','state','zipcode','userkey')
        exclude_fields = ('url')
        read_only_fields = ('userkey',)

class UserProfileURLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('userkey','username','url',)
        read_only_fields = ('userkey',)

class RouteKeeperDeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteKeeperDeviceModel
        fields = ('__all__')
        exclude_fields = ('userkey')
        read_only_fields = ('deviceid',)

class RouteKeeperDeviceHistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteKeeperDeviceHistoryModel
        fields = ('deviceid','statuscode','datetime')
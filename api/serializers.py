from django.contrib.auth.models import User
from rest_framework import serializers
from .models import RouteKeeperDeviceModel, Profile, RouteKeeperDeviceHistoryModel

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','last_login','username','first_name','last_name','email','date_joined','address','city','state','zipcode')
        exclude_fields = ('url')

class UserProfileURLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','username','url')

class RouteKeeperDeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteKeeperDeviceModel
        fields = ('__all__')
        read_only_fields = ('deviceid',)
        # fields = '__all__'

class RouteKeeperDeviceHistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteKeeperDeviceHistoryModel
        fields = ('deviceid','statuscode','datetime')
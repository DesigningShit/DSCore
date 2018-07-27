from django.contrib.auth.models import User
from rest_framework import serializers
from .models import RouteKeeperDeviceModel, Profile, RouteKeeperDeviceHistoryModel, IOTChannelModel, IOTSensorModel, IOTSensorReadingModel

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('last_login','username','first_name','last_name','email','date_joined','address','city','state','zipcode','userkey')
        exclude_fields = ('url')

class UserProfileURLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('userkey','username','url')

class RouteKeeperDeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteKeeperDeviceModel
        fields = ('__all__')
        exclude_fields = ('userkey')
        read_only_fields = ('deviceid',)
        # fields = '__all__'

class RouteKeeperDeviceHistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteKeeperDeviceHistoryModel
        fields = ('deviceid','statuscode','datetime')

class IOTChannelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IOTChannelModel
        fields = ('__all__')

class IOTSensorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IOTSensorModel
        fields = ('__all__')

class IOTSensorReadingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IOTSensorReadingModel
        fields = ('__all__')
        depth = 2

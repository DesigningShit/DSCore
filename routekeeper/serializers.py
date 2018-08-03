from rest_framework import serializers
from .models import RouteKeeperDeviceModel, RouteKeeperDeviceHistoryModel

class RouteKeeperDeviceModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    ipDeviceName = serializers.CharField(required=True)
    ipAddress = serializers.IPAddressField(required=True)
    ipMask = serializers.IPAddressField(required=True)
    ipGateway = serializers.IPAddressField(required=True)
    ipExternalAddress = serializers.IPAddressField(required=True)

    class Meta:
        model = RouteKeeperDeviceModel
        fields = ('name','deviceid','ipDeviceName','ipAddress','ipMask','ipGateway','ipExternalAddress','owner')
        exclude_fields = ('userkey','id')
        read_only_fields = ('deviceid',)

class RouteKeeperDeviceHistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteKeeperDeviceHistoryModel
        fields = ('deviceid','statuscode','datetime')
        read_only_fields = ('datetime',)
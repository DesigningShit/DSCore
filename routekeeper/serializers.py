from rest_framework import serializers as s
from .models import RouteKeeperDeviceModel, RouteKeeperDeviceHistoryModel

class RouteKeeperDeviceModelSerializer(s.ModelSerializer):
    name = s.CharField(required=True)
    ipDeviceName = s.CharField(required=True)
    ipAddress = s.IPAddressField(required=True)
    ipMask = s.IPAddressField(required=True)
    ipGateway = s.IPAddressField(required=True)
    ipExternalAddress = s.IPAddressField(required=True)

    class Meta:
        model = RouteKeeperDeviceModel
        fields = ('name','deviceid','ipDeviceName','ipAddress','ipMask','ipGateway','ipExternalAddress','owner')
        exclude_fields = ('userkey','id')
        read_only_fields = ('deviceid',)

class RouteKeeperDeviceHistoryModelSerializer(s.ModelSerializer):
    class Meta:
        model = RouteKeeperDeviceHistoryModel
        fields = ('deviceid','statuscode','datetime')
        read_only_fields = ('datetime',)
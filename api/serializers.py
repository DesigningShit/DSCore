from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username','password','first_name','last_name','email','date_joined','address','city','state','zipcode','userkey','last_login')
        exclude_fields = ('url')
        read_only_fields = ('userkey','date_joined','last_login')
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileURLSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, help_text='First Name of User')
    last_name = serializers.CharField(required=True, help_text='Last Name of User')
    address = serializers.CharField(required=True, help_text='Street Address of User')
    city = serializers.CharField(required=True, help_text='City of User')
    state = serializers.CharField(required=True, help_text='State of User')
    zipcode = serializers.CharField(required=True, help_text='Zip Code of User')
    email = serializers.EmailField(required=True, help_text='E-Mail Address of User')

    class Meta:
        model = Profile
        fields = ('username','password','first_name','last_name','email','date_joined','address','city','state','zipcode','userkey','last_login')
        read_only_fields = ('userkey','date_joined','last_login')
        extra_kwargs = {'password': {'write_only': True},
                        'first_name': {'write_only': True},
                        'last_name': {'write_only': True},
                        'email': {'write_only': True},
                        'address': {'write_only': True},
                        'city': {'write_only': True},
                        'state': {'write_only': True},
                        'zipcode': {'write_only': True}}
    
    def create(self, validated_data):
        profile = Profile.objects.create_user(**validated_data)
        return profile
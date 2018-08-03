from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from iot.models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel


@login_required
def home(request):
    my_channels = IOTChannelModel.objects.filter(channelowner=request.user)
    my_sensors = IOTSensorModel.objects.filter(channel__channelowner=request.user)

    return render(request, "iot/Home.html",{'mychannels': my_channels,'mysensors':my_sensors})
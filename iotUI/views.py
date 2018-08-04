from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from iot.models import IOTChannelModel, IOTSensorModel, IOTSensorReadingModel


@login_required
def home(request):
    my_channels = IOTChannelModel.objects.filter(channelowner=request.user)
    my_sensors = IOTSensorModel.objects.filter(channel__channelowner=request.user)
    my_data = IOTSensorReadingModel.objects.filter(sensor__channel__channelowner=request.user)

    return render(request, "iot/Home.html",{'mychannels': my_channels,'mysensors':my_sensors,'mydata':my_data,'mychannelcount':my_channels.count(),'mysensorcount':my_sensors.count(),'mydatacount':my_data.count()})

@login_required
def MyChannels(request):
    my_channels = IOTChannelModel.objects.filter(channelowner=request.user)

    return render(request, "iot/channel_list.html",{'mychannels': my_channels,'mychannelcount':my_channels.count()})

@login_required
def MySensors(request):
    my_sensors = IOTSensorModel.objects.filter(channel__channelowner=request.user)

    return render(request, "iot/sensor_list.html",{'mysensors':my_sensors,'mysensorcount':my_sensors.count()})

@login_required
def MyData(request):
    my_data = IOTSensorReadingModel.objects.filter(sensor__channel__channelowner=request.user)

    return render(request, "iot/data_list.html",{'mydata':my_data,'mydatacount':my_data.count()})

"""dscore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from iotUI.views import home, MyChannels, MySensors, MyData, MyProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import urls

urlpatterns = [
    # Route for web based admin page
    path('admin/', admin.site.urls),
    # Route for web based API Auth to local Model
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'accounts/', include('rest_framework.urls')),
    # Route for JSON Web Token based API Auth to local Model
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path(r'api-token-verify/', verify_jwt_token),
    # Routes for RESTful API
    path(r'api/v1/', include('api.urls')),
    path('iot/frontend/', home, name="iot_frontend"),
    path('iot/frontend/channels/', MyChannels, name="iot_frontend_channels"),
    path('iot/frontend/sensors/', MySensors, name="iot_frontend_sensors"),
    path('iot/frontend/data/', MyData, name="iot_frontend_data"),
    path('iot/frontend/profile/', MyProfile, name="iot_frontend_profile"),
]

# Generated by Django 2.0.7 on 2018-07-26 17:13

import api.keygen
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_routekeeperdevicehistorymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routekeeperdevicehistorymodel',
            name='deviceid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.RouteKeeperDeviceModel', to_field='deviceid'),
        ),
        migrations.AlterField(
            model_name='routekeeperdevicemodel',
            name='deviceid',
            field=models.CharField(default=api.keygen.deviceID, max_length=25, unique=True),
        ),
    ]

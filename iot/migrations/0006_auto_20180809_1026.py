# Generated by Django 2.0.7 on 2018-08-09 15:26

import api.keygen
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0005_auto_20180809_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iotchannelmodel',
            name='channelid',
            field=models.CharField(default=api.keygen.getRandomID, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='iotsensormodel',
            name='sensorid',
            field=models.CharField(default=api.keygen.getRandomID, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='iotsensorreadingmodel',
            name='readingid',
            field=models.CharField(default=api.keygen.getRandomID, max_length=30, unique=True),
        ),
    ]

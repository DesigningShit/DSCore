# Generated by Django 2.0.7 on 2018-07-26 17:46

import api.keygen
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180726_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userkey',
            field=models.CharField(default=api.keygen.deviceID, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='routekeeperdevicemodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, to_field='userkey'),
        ),
    ]

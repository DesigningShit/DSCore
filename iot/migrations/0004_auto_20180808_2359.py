# Generated by Django 2.0.7 on 2018-08-09 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0003_auto_20180808_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iottenant',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TenantOwner', to=settings.AUTH_USER_MODEL, to_field='userkey'),
        ),
    ]

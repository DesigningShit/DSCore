# Generated by Django 2.0.7 on 2018-08-03 05:14

import api.keygen
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0002_remove_iotsensorreadingmodel_readingid'),
    ]

    operations = [
        migrations.AddField(
            model_name='iotsensorreadingmodel',
            name='readingid',
            field=models.CharField(default=api.keygen.dataID, max_length=30),
        ),
    ]
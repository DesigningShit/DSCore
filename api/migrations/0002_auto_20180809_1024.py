# Generated by Django 2.0.7 on 2018-08-09 15:24

import api.keygen
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userkey',
            field=models.CharField(default=api.keygen.getRandomID, max_length=20, unique=True),
        ),
    ]

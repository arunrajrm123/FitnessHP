# Generated by Django 4.2.1 on 2023-09-24 14:02

import backend.models
import datetime
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_alter_useraccount_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='last_login',
            field=backend.models.CustomDateTimeField(default=datetime.datetime(2023, 9, 24, 14, 2, 24, tzinfo=datetime.timezone.utc)),
        ),
    ]

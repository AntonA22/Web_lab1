# Generated by Django 4.2.7 on 2024-09-19 06:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_flight_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 6, 55, 57, 936910, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]

# Generated by Django 4.2.7 on 2024-10-08 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_flight_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 8, 10, 28, 39, 642239, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]
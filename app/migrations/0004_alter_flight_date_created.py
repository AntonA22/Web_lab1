# Generated by Django 4.2.7 on 2024-09-19 06:46

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
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 6, 46, 19, 491570, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]
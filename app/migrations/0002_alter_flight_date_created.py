# Generated by Django 4.2.7 on 2024-10-22 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 22, 11, 29, 43, 603211, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]

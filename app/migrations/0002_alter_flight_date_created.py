# Generated by Django 4.2.7 on 2024-10-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date_created',
            field=models.DateTimeField(verbose_name='Дата создания'),
        ),
    ]
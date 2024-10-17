# Generated by Django 4.2.16 on 2024-10-17 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Введён'), (2, 'В работе'), (3, 'Завершен'), (4, 'Отклонен'), (5, 'Удален')], default=1, verbose_name='Статус')),
                ('date_created', models.DateTimeField(verbose_name='Дата создания')),
                ('date_formation', models.DateTimeField(blank=True, null=True, verbose_name='Дата формирования')),
                ('date_complete', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения')),
                ('launch_cosmodrom', models.CharField(blank=True, null=True)),
                ('arrival_cosmodrom', models.CharField(blank=True, null=True)),
                ('estimated_launch_date', models.DateTimeField(blank=True, null=True)),
                ('moderator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='moderator', to=settings.AUTH_USER_MODEL, verbose_name='Модератор')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Перелет',
                'verbose_name_plural': 'Перелеты',
                'db_table': 'flights',
                'ordering': ('-date_formation',),
            },
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('status', models.IntegerField(choices=[(1, 'Действует'), (2, 'Удалена')], default=1, verbose_name='Статус')),
                ('image', models.ImageField(default='images/default.png', upload_to='')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('creation_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Космический корабль',
                'verbose_name_plural': 'Космические корабли',
                'db_table': 'ships',
            },
        ),
        migrations.CreateModel(
            name='ShipFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='Поле м-м')),
                ('flight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.flight')),
                ('ship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.ship')),
            ],
            options={
                'verbose_name': 'м-м',
                'verbose_name_plural': 'м-м',
                'db_table': 'ship_flight',
                'unique_together': {('ship', 'flight')},
            },
        ),
    ]

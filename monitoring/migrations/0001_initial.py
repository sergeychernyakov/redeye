# Generated by Django 5.1.1 on 2024-09-16 18:46

import django.db.models.deletion
import monitoring.models.floor
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=monitoring.models.floor.floor_image_upload_path, verbose_name='Схема этажа')),
                ('order', models.PositiveIntegerField(verbose_name='Порядок этажа')),
            ],
            options={
                'verbose_name': 'Этаж',
                'verbose_name_plural': 'Этажи',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название карты')),
                ('map_type', models.CharField(choices=[('underlay', 'Подложка'), ('yandex', 'Яндекс Карта')], max_length=20, verbose_name='Тип карты')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название объекта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.CreateModel(
            name='Detector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('port', models.PositiveIntegerField(verbose_name='Порт')),
                ('internal_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Внутренний идентификатор')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('web_interface_url', models.URLField(blank=True, null=True, verbose_name='URL веб-интерфейса')),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Серийный номер')),
                ('rtsp_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='RTSP URL')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя пользователя RTSP')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='Пароль RTSP')),
                ('vpn_server_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP VPN сервера')),
                ('vpn_username', models.CharField(blank=True, max_length=100, null=True, verbose_name='VPN Логин')),
                ('vpn_password', models.CharField(blank=True, max_length=100, null=True, verbose_name='VPN Пароль')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('image_port', models.PositiveIntegerField(blank=True, null=True, verbose_name='Порт изображения')),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Производитель')),
                ('model', models.CharField(default='SmartVision3', max_length=100, verbose_name='Модель')),
                ('detector_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип')),
                ('access_group', models.CharField(blank=True, max_length=100, null=True, verbose_name='Группа доступа')),
                ('camera', models.CharField(blank=True, max_length=100, null=True, verbose_name='Камера')),
                ('controller', models.CharField(blank=True, max_length=100, null=True, verbose_name='Контроллер')),
                ('floor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detectors', to='monitoring.floor')),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detectors', to='monitoring.map')),
            ],
            options={
                'verbose_name': 'Детектор',
                'verbose_name_plural': 'Детекторы',
            },
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('detector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.detector')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Инцидент',
                'verbose_name_plural': 'Инциденты',
            },
        ),
        migrations.AddField(
            model_name='floor',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floors', to='monitoring.map'),
        ),
        migrations.AddField(
            model_name='map',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='monitoring.object'),
        ),
    ]

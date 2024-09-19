# Generated by Django 5.1.1 on 2024-09-19 10:16

import colorfield.fields
import django.db.models.deletion
import monitoring.models.area
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=monitoring.models.area.area_image_upload_path, verbose_name='Схема этажа')),
                ('order', models.PositiveIntegerField(verbose_name='Порядок этажа')),
                ('background_color', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None, verbose_name='Цвет подложки')),
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
                ('detector_type', models.CharField(choices=[('animal', 'Животное'), ('plant', 'Растение')], default='animal', max_length=100, verbose_name='Тип детектора')),
                ('access_group', models.CharField(blank=True, max_length=100, null=True, verbose_name='Группа доступа')),
                ('camera', models.CharField(blank=True, max_length=100, null=True, verbose_name='Камера')),
                ('controller', models.CharField(blank=True, max_length=100, null=True, verbose_name='Контроллер')),
                ('media_file', models.FileField(blank=True, null=True, upload_to='detector_media/', verbose_name='Фото или Видео')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detectors', to='monitoring.area')),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detectors', to='monitoring.map')),
            ],
            options={
                'verbose_name': 'Камера',
                'verbose_name_plural': 'Камеры',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='monitoring.map'),
        ),
        migrations.AddField(
            model_name='map',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='monitoring.object'),
        ),
    ]

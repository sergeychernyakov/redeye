# src/monitoring/management/commands/seeder.py

import os
import shutil
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from monitoring.models import Object, Map, Area, Detector
import random
from PIL import Image  # Подключаем Pillow для работы с изображениями
from faker import Faker
import logging

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.faker = Faker('ru_RU')  # Russian humor!

        # 1. Создание суперпользователей
        self.create_superusers()

        # 2. Создание объекта "Москворецкий парк"
        self.create_moskvoretsky_park()

        self.stdout.write(self.style.SUCCESS(f'Данные успешно загружены'))

    def create_superusers(self):
        # Создание суперпользователя Сергей Черняков
        if not User.objects.filter(username='sergeychernyakov').exists():
            User.objects.create_superuser(
                username='sergeychernyakov',
                email='chernyakov.sergey@gmail.com',
                password='JKLkjhlI9;sss',
                first_name='Сергей',
                last_name='Черняков'
            )
            self.stdout.write(self.style.SUCCESS('Суперпользователь Сергей Черняков создан'))

        # Создание суперпользователя Михаил Маркуцин
        if not User.objects.filter(username='markutsin').exists():
            User.objects.create_superuser(
                username='markutsin',
                email='markutsin@gmail.com',
                password='HKPJk999;qq',
                first_name='Михаил',
                last_name='Маркуцин'
            )
            self.stdout.write(self.style.SUCCESS('Суперпользователь Михаил Маркуцин создан'))

        # Создание суперпользователя Михаил Маркуцин
        if not User.objects.filter(username='markutsin').exists():
            User.objects.create_superuser(
                username='test1',
                email='test1@gmail.com',
                password='KJL23LKJ;l',
                first_name='Test',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS('Суперпользователь Test User создан'))

    def create_moskvoretsky_park(self):
        # Создание объекта "Москворецкий парк"
        park = Object.objects.create(
            name="Москворецкий парк",
            address="Москва, Россия",
            description="Национальный парк с краснокнижными видами растений и животных",
            latitude=55.7412,
            longitude=37.6163
        )
        self.stdout.write(self.style.SUCCESS(f'Объект {park.name} создан'))

        # Создание карты подложки "Москворецкий парк"
        park_map = Map.objects.create(
            name="Москворецкий парк",
            map_type="underlay",  # Тип карты подложка
            object=park
        )
        self.stdout.write(self.style.SUCCESS(f'Карта подложка {park_map.name} создана'))

        # Путь к изображению схемы парка
        park_image = 'monitoring/static/img/area-plan.jpeg'

        # Определяем путь к изображению в папке media
        media_image_path = os.path.join(settings.MEDIA_ROOT, f'maps/{park_map.id}/areas/{os.path.basename(park_image)}')

        image_width, image_height = self.get_image_size(park_image)

        # Копируем изображение из static в media
        os.makedirs(os.path.dirname(media_image_path), exist_ok=True)
        shutil.copyfile(park_image, media_image_path)

        # Создание подложки (схемы парка)
        area = Area.objects.create(
            map=park_map,
            image=f'maps/{park_map.id}/areas/{os.path.basename(park_image)}',
            order=1,
            background_color="#FFFFFF"  # Зеленый цвет фона для парка
        )
        self.stdout.write(self.style.SUCCESS(f'Схема парка добавлена как подложка для карты {park_map.name}'))

        # Добавляем камеры краснокнижных животных
        self.add_detectors_to_area(area, image_width, image_height, detector_type='animal')

    def get_image_size(self, image_path):
        """Получаем ширину и высоту изображения."""
        try:
            with Image.open(image_path) as img:
                return img.width, img.height
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при получении размера изображения: {e}"))
            return 1000, 800  # Значения по умолчанию, если что-то пошло не так

    def add_detectors_to_area(self, area, image_width, image_height, detector_type='animal'):
        # Задаем минимальные и максимальные значения для координат (широта и долгота)
        min_latitude = 0
        max_latitude = image_height  # Ограничение по высоте изображения
        min_longitude = 0
        max_longitude = image_width   # Ограничение по ширине изображения

        num_detectors = random.randint(3, 10)  # Случайное количество камер
        for _ in range(num_detectors):
            try:
                detector = Detector.objects.create(
                    name=f"Детектор {random.randint(1, 1000)}",
                    map=area.map,
                    area=area,  # Привязка камеры к схеме парка
                    ip='192.168.9.161',
                    port=554,
                    rtsp_url='rtsp://admin:campass911@192.168.9.161:554/stream1',
                    vpn_server_ip='178.209.97.254',
                    vpn_username='argo1',
                    vpn_password='X9eDB@Mxp_',
                    latitude=random.uniform(min_latitude, max_latitude),
                    longitude=random.uniform(min_longitude, max_longitude),
                    detector_type=detector_type  # Тип камеры (животное или растение)
                )
                detector.save()

                # Log detector creation
                logging.info(f"Created detector {detector.name} on area {area.order}")

            except Exception as e:
                # Log any errors during detector creation
                logging.error(f"Error creating detector on area {area.order}: {e}")

# Example usage:
# python3 -m src.monitoring.management.commands.seeder

if __name__ == '__main__':
    print("This is a management command for seeding the database. Use it with `python manage.py seeder`.")
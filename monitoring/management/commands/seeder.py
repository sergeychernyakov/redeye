# monitoring/management/commands/seeder.py

import os
import shutil
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from monitoring.models import Object, Map, Area, Detector
import random
from PIL import Image  # Подключаем Pillow для работы с изображениями
from django.utils import timezone
from faker import Faker
import logging

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.faker = Faker('ru_RU')  # Russian humor!

        # 1. Создание двух суперпользователей
        self.create_superusers()

        # 2. Создание 20 обычных пользователей (сотрудников)
        self.create_employees()

        # 3. Создание объекта "Торговый центр Кловер"
        self.create_clover_mall()

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

    def create_employees(self):
        # Юмористические имена пользователей
        funny_names = [
            "Василий Полуночник", "Ольга Шумахер", "Евгений Трудоголик", "Мария Знайка",
            "Петр Весельчак", "Анна Рокстар", "Георгий Тормозов", "Людмила Дрифт", 
            "Иван Грозный", "Татьяна Громова", "Алексей Безумный", "Дарья Пирожкова",
            "Максим Безопасный", "Наталья Храбрая", "Семен Ленивый", "Екатерина Буря",
            "Федор Счастливый", "Николай Шумный", "Юлия Молниеносная", "Светлана Загадочная"
        ]

        # Создание 20 обычных пользователей (сотрудников) без права логина
        for name in funny_names:
            first_name, last_name = name.split()
            username = f'employee_{random.randint(1000, 9999)}'
            email = f'{username}@company.com'

            user = User.objects.create(
                is_staff=False,
                is_superuser=False,
                is_active=False,  # Без права логина
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                last_login=None,
            )

        self.stdout.write(self.style.SUCCESS('20 сотрудников созданы и добавлены в группу'))

    def create_clover_mall(self):
        # Создание объекта "Торговый центр Кловер"
        mall = Object.objects.create(
            name="Торговый центр Кловер",
            address="г. Калининград, пл. Победы, д.10",
            description="Огромный торговый центр с множеством этажей и магазинов",
            latitude=54.7104,
            longitude=20.4522
        )
        self.stdout.write(self.style.SUCCESS(f'Объект {mall.name} создан'))

        # Создание карты "Торговый центр"
        mall_map = Map.objects.create(
            name="Торговый центр",
            map_type="underlay",
            object=mall
        )
        self.stdout.write(self.style.SUCCESS(f'Карта {mall_map.name} создана'))

        # Пути к изображениям этажей
        areas_images = [
            'monitoring/static/img/clover-first-area-plan.png',
            'monitoring/static/img/clover-second-area-plan.png',
            'monitoring/static/img/clover-third-area-plan.png',
        ]

        for i, area_image in enumerate(areas_images, start=1):
            # Определяем путь к изображению в папке media
            media_image_path = os.path.join(settings.MEDIA_ROOT, f'maps/{mall_map.id}/areas/{os.path.basename(area_image)}')
            
            image_width, image_height = self.get_image_size(area_image)

            # Копируем изображение из static в media
            os.makedirs(os.path.dirname(media_image_path), exist_ok=True)
            shutil.copyfile(area_image, media_image_path)

            # Создание этажа
            area = Area.objects.create(
                map=mall_map,
                image=f'maps/{mall_map.id}/areas/{os.path.basename(area_image)}',
                order=i,
                background_color="#F5F6FA"
            )
            # Добавляем 3-10 детекторов на каждый этаж
            self.add_detectors_to_area(area, image_width, image_height)
            
            self.stdout.write(self.style.SUCCESS(f'Этаж {i} добавлен для карты {mall_map.name}'))

    def get_image_size(self, image_path):
        """Получаем ширину и высоту изображения."""
        try:
            with Image.open(image_path) as img:
                return img.width, img.height
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при получении размера изображения: {e}"))
            return 1000, 800  # Значения по умолчанию, если что-то пошло не так

    def add_detectors_to_area(self, area, image_width, image_height):
        # Задаем минимальные и максимальные значения для координат (широта и долгота)
        min_latitude = 0
        max_latitude = image_height  # Ограничение по высоте изображения
        min_longitude = 0
        max_longitude = image_width   # Ограничение по ширине изображения

        num_detectors = random.randint(3, 10)  # Случайное количество детекторов
        for _ in range(num_detectors):
            try:
                detector = Detector.objects.create(
                    name=f"Детектор {random.randint(1, 1000)}",
                    map=area.map,
                    area=area,  # Привязка детектора к этажу
                    ip='192.168.9.161',
                    port=554,
                    rtsp_url='rtsp://admin:campass911@192.168.9.161:554/stream1',
                    vpn_server_ip='178.209.97.254',
                    vpn_username='argo1',
                    vpn_password='X9eDB@Mxp_',
                    latitude=random.uniform(min_latitude, max_latitude),
                    longitude=random.uniform(min_longitude, max_longitude)
                )
                detector.save()

                # Log detector creation
                logging.info(f"Created detector {detector.name} on area {area.order}")

            except Exception as e:
                # Log any errors during detector creation
                logging.error(f"Error creating detector on area {area.order}: {e}")


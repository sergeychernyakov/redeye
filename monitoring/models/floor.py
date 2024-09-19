# monitoring/models/floor.py

from django.db import models
import os
from django.utils.html import mark_safe
from colorfield.fields import ColorField
from django.apps import apps

def floor_image_upload_path(instance: 'Floor', filename: str) -> str:
    """ Генерация пути для сохранения изображения: maps/{map_id}/floors/{filename} """
    return os.path.join(f'maps/{instance.map.id}/floors/', filename)

class Floor(models.Model):
    map = models.ForeignKey('Map', on_delete=models.CASCADE, related_name="floors")  # Связь с картой
    image = models.ImageField("Схема этажа", upload_to=floor_image_upload_path)  # Динамическое сохранение изображений
    order = models.PositiveIntegerField("Порядок этажа")  # Поле для хранения порядка этажей
    background_color = ColorField("Цвет подложки", default="#ffffff")  # Цвет фона подложки с выбором цвета

    class Meta:
        verbose_name = "Этаж"
        verbose_name_plural = "Этажи"
        ordering = ['order']  # Автоматическая сортировка по порядку

    def __str__(self) -> str:
        return f"Этаж {self.order} карты {self.map.name}"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="300" height="auto" />')
        return "No Image Available"
    
    image_tag.short_description = "Этаж"

    @property
    def incidents(self):
        """Получить все инциденты, связанные с детекторами на этом этаже"""
        Incident = apps.get_model('monitoring', 'Incident')
        return Incident.objects.filter(detector__in=self.detectors.all()) 

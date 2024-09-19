# monitoring/models/map.py

from django.db import models
from .object import Object
from django.apps import apps

class Map(models.Model):
    MAP_TYPE_CHOICES = [
        ('underlay', 'Подложка'),
        ('yandex', 'Яндекс Карта'),
    ]
    
    name = models.CharField("Название карты", max_length=255)
    map_type = models.CharField("Тип карты", max_length=20, choices=MAP_TYPE_CHOICES)
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name="maps")  # Связь с объектом

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"

    def __str__(self):
        return f"{self.name} ({self.get_map_type_display()})"

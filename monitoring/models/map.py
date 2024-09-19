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

    @property
    def incidents(self):
        """
        Get all incidents related to the detectors on this map.
        We gather detectors both directly linked to the map and those on the map's floors.
        """
        # Directly linked detectors
        detectors = self.detectors.all()

        # Detectors on the map's floors
        Detector = apps.get_model('monitoring', 'Detector')
        floor_detectors = Detector.objects.filter(floor__in=self.floors.all())

        # Combine both sets of detectors and get incidents
        Incident = apps.get_model('monitoring', 'Incident')
        return Incident.objects.filter(detector__in=detectors | floor_detectors)

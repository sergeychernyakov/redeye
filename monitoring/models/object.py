# monitoring/models/object.py

from django.db import models

class Object(models.Model):
    name = models.CharField("Название объекта", max_length=255)
    description = models.TextField("Описание", blank=True, null=True)

    # Дополнительные необязательные поля
    address = models.CharField("Адрес", max_length=255, blank=True, null=True)  # Адрес объекта
    latitude = models.FloatField("Широта", blank=True, null=True)  # Широта объекта
    longitude = models.FloatField("Долгота", blank=True, null=True)  # Долгота объекта

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"

    def __str__(self):
        return self.name

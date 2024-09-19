# monitoring/models/detector.py

from django.db import models
from django.core.exceptions import ValidationError
from .map import Map
from .floor import Floor

class Detector(models.Model):
    class Meta:
        verbose_name = "Детектор"
        verbose_name_plural = "Детекторы"
    
    # Основные поля камеры
    name = models.CharField("Название", max_length=100)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name="detectors")  # Связь с картой
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name="detectors", blank=True, null=True)  # Связь с этажом (опционально)
    ip = models.GenericIPAddressField("IP", protocol="both", unpack_ipv4=False)
    port = models.PositiveIntegerField("Порт")
    internal_id = models.CharField("Внутренний идентификатор", max_length=100, blank=True, null=True)
    address = models.CharField("Адрес", max_length=255, blank=True, null=True)
    web_interface_url = models.URLField("URL веб-интерфейса", blank=True, null=True)
    serial_number = models.CharField("Серийный номер", max_length=100, blank=True, null=True)
    
    # Параметры RTSP подключения
    rtsp_url = models.CharField("RTSP URL", max_length=255, blank=True, null=True)
    username = models.CharField("Имя пользователя RTSP", max_length=100, blank=True, null=True)
    password = models.CharField("Пароль RTSP", max_length=100, blank=True, null=True)

    # Параметры PPTP VPN
    vpn_server_ip = models.GenericIPAddressField("IP VPN сервера", protocol="both", unpack_ipv4=False, blank=True, null=True)
    vpn_username = models.CharField("VPN Логин", max_length=100, blank=True, null=True)
    vpn_password = models.CharField("VPN Пароль", max_length=100, blank=True, null=True)

    # Координаты и другие параметры
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    image_port = models.PositiveIntegerField("Порт изображения", blank=True, null=True)
    manufacturer = models.CharField("Производитель", max_length=100, blank=True, null=True)
    model = models.CharField("Модель", max_length=100, default="SmartVision3")
    detector_type = models.CharField("Тип", max_length=100, blank=True, null=True)
    access_group = models.CharField("Группа доступа", max_length=100, blank=True, null=True)
    camera = models.CharField("Камера", max_length=100, blank=True, null=True)
    controller = models.CharField("Контроллер", max_length=100, blank=True, null=True)

    # def clean(self) -> None:
    #     """
    #     Проверка: камеры могут быть привязаны только к картам типа "Яндекс".
    #     """
    #     if self.map.map_type != 'yandex':
    #         raise ValidationError("Камеры могут быть привязаны только к картам типа 'Яндекс'.")

    def __str__(self) -> str:
        return f"{self.ip}:{self.port} - {self.internal_id or 'No ID'}"

# Example usage:
# python3 -m src.monitoring.models.detector

if __name__ == '__main__':
    print("This is a model file. To test or interact with it, use Django's shell or admin interface.")

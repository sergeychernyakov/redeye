# monitoring/models/incident.py

from django.db import models
from .detector import Detector
from django.contrib.auth.models import User

class Incident(models.Model):
    detector = models.ForeignKey(Detector, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Инцидент"
        verbose_name_plural = "Инциденты"

    def __str__(self):
        return f"Incident at {self.detector.name} on {self.timestamp}"

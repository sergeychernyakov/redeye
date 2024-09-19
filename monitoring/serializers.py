# monitoring/serializers.py

from rest_framework import serializers
from .models import Object, Map, Area, Detector

# 1. ObjectSerializer
class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ['id', 'name', 'address', 'description', 'latitude', 'longitude']  # Указываем нужные поля


# 2. MapSerializer
class MapSerializer(serializers.ModelSerializer):
    object = ObjectSerializer(read_only=True)  # Вложенный сериализатор для Object

    class Meta:
        model = Map
        fields = ['id', 'name', 'map_type', 'object']  # Указываем нужные поля


# 3. AreaSerializer
class AreaSerializer(serializers.ModelSerializer):
    map = MapSerializer(read_only=True)  # Вложенный сериализатор для Map

    class Meta:
        model = Area
        fields = ['id', 'map', 'image', 'order']  # Указываем нужные поля


# 4. DetectorSerializer
class DetectorSerializer(serializers.ModelSerializer):
    map = MapSerializer(read_only=True)  # Вложенный сериализатор для Map

    class Meta:
        model = Detector
        fields = [
            'id', 'name', 'map', 'ip', 'port', 'internal_id', 'address', 'web_interface_url',
            'serial_number', 'rtsp_url', 'username', 'password', 'vpn_server_ip', 'vpn_username',
            'vpn_password', 'latitude', 'longitude', 'image_port', 'manufacturer', 'model',
            'detector_type', 'access_group', 'camera', 'controller'
        ]  # Указываем все нужные поля

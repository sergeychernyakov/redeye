# monitoring/forms/detector_form.py

from django import forms
from monitoring.models import Detector

class DetectorForm(forms.ModelForm):
    class Meta:
        model = Detector
        fields = [
            'name', 'area', 'ip', 'port', 'internal_id', 'address', 'web_interface_url', 
            'serial_number', 'rtsp_url', 'username', 'password', 'vpn_server_ip',
            'vpn_username', 'vpn_password', 'latitude', 'longitude',
            'image_port', 'manufacturer', 'model', 'detector_type', 'access_group',
            'camera', 'controller'
        ]
        widgets = {
            'password': forms.PasswordInput(),  # скрытие пароля для RTSP
            'vpn_password': forms.PasswordInput(),  # скрытие пароля для VPN
        }

    # Проверка для RTSP URL
    def clean_rtsp_url(self):
        rtsp_url = self.cleaned_data.get('rtsp_url')
        if rtsp_url and not rtsp_url.startswith('rtsp://'):
            raise forms.ValidationError("RTSP URL должен начинаться с rtsp://")
        return rtsp_url

    # Проверка для IP-адреса
    def clean_ip(self):
        ip = self.cleaned_data.get('ip')
        if not ip:
            raise forms.ValidationError("IP-адрес обязателен для заполнения.")
        return ip

    # Проверка для порта
    def clean_port(self):
        port = self.cleaned_data.get('port')
        if port <= 0 or port > 65535:
            raise forms.ValidationError("Введите корректный номер порта (от 1 до 65535).")
        return port

    # Проверка для VPN IP-адреса
    def clean_vpn_server_ip(self):
        vpn_server_ip = self.cleaned_data.get('vpn_server_ip')
        if vpn_server_ip and not vpn_server_ip.strip():
            raise forms.ValidationError("VPN IP не может быть пустым.")
        return vpn_server_ip

    # Дополнительная проверка для широты (latitude) и долготы (longitude)
    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')
        return longitude

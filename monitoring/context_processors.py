# monitoring/context_processors.py

from django.conf import settings

def api_keys(request):
    return {
        'YANDEX_API_KEY': settings.YANDEX_API_KEY,
    }

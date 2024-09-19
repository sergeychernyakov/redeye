from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import Detector, Map, Object, Area

# Переопределяем заголовок и заголовок страницы администрирования
admin.site.site_header = "Панель администратора"
admin.site.site_title = "Панель администратора"
admin.site.index_title = "Добро пожаловать в панель администратора"

# Отменяем регистрацию стандартной модели User
admin.site.unregister(User)

# Регистрируем модель User с кастомным UserAdmin
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональные данные', {'fields': ('first_name', 'last_name', 'email')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )

# Настройка отображения модели Object в админке
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude')
    search_fields = ('name', 'address')

# Настройка отображения модели Map в админке
class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'map_type', 'object')
    list_filter = ('map_type',)
    search_fields = ('name', 'object__name')

class AreaAdmin(admin.ModelAdmin):
    list_display = ('map', 'order', 'image_thumbnail')
    readonly_fields = ['image_thumbnail']
    fields = ('map', 'order', 'background_color', 'image_thumbnail')

    # Отображение уменьшенного изображения
    def image_thumbnail(self, obj):
        if obj.image:
            # Отображение уменьшенного изображения, при клике на которое откроется модальное окно
            return format_html(
                f'<a href="javascript:void(0);" onclick="showModal(\'{obj.image.url}\');">'
                f'<img src="{obj.image.url}" width="200" height="auto" /></a>'
            )
        return "Нет изображения"

    image_thumbnail.short_description = 'Предпросмотр'

    class Media:
        # Подключаем кастомный JS файл для модального окна
        js = ('admin/js/area_image_modal.js',)

# Настройка отображения модели Detector в админке
class DetectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'port', 'map')
    search_fields = ('name', 'ip', 'map__name')
    list_filter = ('map',)

# Регистрация моделей с настройками
admin.site.register(User, UserAdmin)
admin.site.register(Object, ObjectAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Detector, DetectorAdmin)

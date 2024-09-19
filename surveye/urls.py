# surveye/urls.py

"""
URL configuration for surveye project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from monitoring.views import floor_plan, yandex_map, home_redirect
from monitoring.views import MapDetailView, ObjectCreateView, MapCreateView
from monitoring.views import DetectorCreateView, DetectorUpdateView, DetectorDetailView

urlpatterns = [
    path('', home_redirect, name='home'),
    
    path('floor-plan/', floor_plan, name='floor_plan'),
    path('yandex-map/', yandex_map, name='yandex_map'),

    # Админка
    path('admin/', admin.site.urls),

    # Логин и логаут
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # URL for creating a new detector
    path('maps/<int:map_id>/detectors/new/', DetectorCreateView.as_view(), name='create_detector'),

    # URL for editing an existing detector
    path('maps/<int:map_id>/detectors/<int:pk>/edit/', DetectorUpdateView.as_view(), name='edit_detector'),

    # URL for displaying a detector's details
    path('maps/<int:map_id>/detectors/<int:pk>/', DetectorDetailView.as_view(), name='show_detector'),

    # Страница создания объекта
    path('objects/new/', ObjectCreateView.as_view(), name='object_create'),
    
    # Страница создания карты для конкретного объекта
    path('objects/<int:object_id>/maps/new/', MapCreateView.as_view(), name='map_create'),
    
    # Страница деталей карты
    path('maps/<int:pk>/', MapDetailView.as_view(), name='map_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

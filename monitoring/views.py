# monitoring/views.py
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Map, Floor, Object, Detector
from django.core.serializers.json import DjangoJSONEncoder
from .forms import DetectorForm
import json

class MapDetailView(DetailView):
    model = Map
    context_object_name = 'map'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Получаем первый этаж, связанный с этой картой
        floor = Floor.objects.filter(map=self.object).first()
        
        if floor and floor.image:
            detectors = floor.detectors.all()
            detectors_data = list(detectors.values('name', 'latitude', 'longitude'))
            
            context['floor_image_url'] = floor.image.url
            context['floor_image_width'] = floor.image.width  # Используем размеры изображения
            context['floor_image_height'] = floor.image.height
            context['floor'] = floor
            context['detectors_json'] = json.dumps(detectors_data, cls=DjangoJSONEncoder)
        else:
            context['floor'] = None
            context['floor_image_url'] = None
            context['detectors_json'] = "[]"

        return context

    def get_template_names(self):
        if self.object.map_type == 'yandex':
            return ['maps/yandex-map.html']
        else:
            return ['maps/floor-plan.html']

class MapCreateView(CreateView):
    model = Map
    fields = ['name', 'map_type']  # Поля, которые будут отображены в форме
    template_name = 'maps/map_form.html'  # Шаблон для отображения формы

    def form_valid(self, form):
        # Получаем объект, к которому будет привязана карта
        object_id = self.kwargs['object_id']
        form.instance.object = Object.objects.get(id=object_id)
        return super().form_valid(form)

    def get_success_url(self):
        # После успешного создания карты перенаправляем на страницу её деталей
        return reverse_lazy('map_detail', kwargs={'pk': self.object.pk})

class ObjectCreateView(CreateView):
    model = Object  # Модель, с которой мы работаем
    fields = ['name', 'address', 'description', 'latitude', 'longitude']  # Поля, которые будут отображены в форме
    template_name = 'objects/object_form.html'  # Шаблон для отображения формы
    success_url = reverse_lazy('object_list')  # URL, куда перенаправить после успешного создания объекта

class DetectorCreateView(CreateView):
    model = Detector
    form_class = DetectorForm
    template_name = 'detectors/new.html'

    def dispatch(self, request, *args, **kwargs):
        print("!!! dispatch method called")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("Form POST data:", request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Assign the map before saving
        map_id = self.kwargs['map_id']
        
        form.instance.map = get_object_or_404(Map, id=map_id)
        
        # Print POST data for debugging purposes
        print("Form POST data:", self.request.POST)
        print(f"Assigned Map ID: {form.instance.map.id}")
        
        return super().form_valid(form)

    def form_invalid(self, form):
        # Print the form errors to help debug the issue
        print("Form errors:", form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        map_id = self.kwargs['map_id']
        context['map'] = get_object_or_404(Map, id=map_id)
        return context
    
    def get_success_url(self):
        # Используем self.object, чтобы получить только что созданный объект Detector
        map_id = self.object.map.id
        return reverse('map_detail', kwargs={'pk': map_id})

class DetectorUpdateView(UpdateView):
    model = Detector
    form_class = DetectorForm
    template_name = 'detectors/edit.html'
    success_url = reverse_lazy('detector_list')  # Replace with your desired URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map_id'] = self.kwargs['map_id']
        return context

class DetectorDetailView(DetailView):
    model = Detector
    template_name = 'detectors/show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map_id'] = self.kwargs['map_id']
        return context

def home_redirect(request):
    if request.user.is_authenticated:
        # Находим последнюю карту
        last_map = Map.objects.order_by('-id').first()
        
        if last_map:
            # Перенаправляем на RESTful URL карты
            return redirect(f'/maps/{last_map.id}/')
        
        # Если карт нет, проверяем наличие объектов
        last_object = Object.objects.order_by('-id').first()
        
        if last_object:
            # Перенаправляем на страницу создания карты для конкретного объекта
            return redirect(f'/objects/{last_object.id}/maps/new/')
        
        # Если объектов нет, перенаправляем на страницу создания объекта
        return redirect('/objects/new/')
    
    # Если пользователь не залогинен, перенаправляем на логин
    return redirect('login')

# Представление для главной страницы, доступное только авторизованным пользователям
@login_required
def floor_plan(request):
    return render(request, 'maps/floor-plan.html')

@login_required
def yandex_map(request):
    return render(request, 'maps/yandex-map.html')


from django.views.generic import CreateView, ListView, DetailView
from .models import Car
from django.urls import reverse_lazy


class CarsCreateView(CreateView):
    model = Car
    template_name = "car_new.html"
    fields = '__all__'
    success_url = reverse_lazy('home')


class CarsListView(ListView):
    model = Car
    template_name = "home.html"


class CarsDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CarsCreateView, CarsListView, CarsDetailView

urlpatterns = [
    path('cars/new/', CarsCreateView.as_view(), name="car_new"),
    path('', CarsListView.as_view(), name="home"),
    path('cars/<int:pk>/', CarsDetailView.as_view(), name="car_detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

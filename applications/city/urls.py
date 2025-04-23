from rest_framework.routers import DefaultRouter

from django.urls import path, include
from . import views

router = DefaultRouter()

router.register(r'cities', views.CityViewSet, basename='cities')
router.register(r'city', views.CityListViewSet, basename='list-city')
router.register(r'city', views.CityReportViewSet, basename='city-report')

urlpatterns = [
    path('', include(router.urls)),
]
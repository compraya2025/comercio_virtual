from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'taxes', views.TaxViewSet, basename='taxes')

urlpatterns = [
    path('', include(router.urls))
]
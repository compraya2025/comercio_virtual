from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'stores', views.StoreViewSet, basename="store")
router.register(r'stores-filter', views.StoreFilterViewSet, basename="store-filter")
router.register(r'stores-report', views.StoreFilterViewSet, basename="store-report")

urlpatterns = [
    path('', include(router.urls)),
]
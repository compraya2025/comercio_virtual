from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register(r'customers', views.CustomersViewSet, basename="customers")


urlpatterns = [
    path('', include(router.urls)),
]
from rest_framework.routers import DefaultRouter

from django.urls import path, include
from . import views

router = DefaultRouter()

router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'category-report', views.CategoryReportViewSet, basename='category-report')

urlpatterns = [
    path('', include(router.urls)),
]
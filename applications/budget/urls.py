from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import  BudgetsViewSet

router = DefaultRouter()

router.register(r'budgets',  BudgetsViewSet, basename='budget')

urlpatterns = [
    path('', include(router.urls)),
]
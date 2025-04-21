from rest_framework.routers import DefaultRouter

from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet, basename='departments')
router.register(r'departments-report', views.DepartmentReportViewSet, basename='department-report')
router.register(r'department', views.DepartmentListViewSet, basename='list-department')

urlpatterns = [
    path('', include(router.urls)),
]
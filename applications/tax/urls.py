from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'taxes', views.TaxViewSet, basename='taxes')
router.register(r'taxes-filter', views.TaxesListViewSet, basename='list-taxes')
router.register(r'taxes-report', views. TaxeReportViewSet, basename='taxes-reporte')

urlpatterns = [
    path('', include(router.urls))
]
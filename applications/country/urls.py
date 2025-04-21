from rest_framework.routers import DefaultRouter
#
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet, basename='countries')
router.register(r'country-report', views.CountryReportViewSet, basename='country-report')

urlpatterns = [
    path('', include(router.urls)),
]
   


from rest_framework.routers import DefaultRouter
#
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet, basename='countries')

urlpatterns = [
    path('', include(router.urls)),
]
   


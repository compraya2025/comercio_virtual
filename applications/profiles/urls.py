from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'profiles', views.ProfileViewSet, basename="profiles")
router.register(r'perfil', views.ProfilesViewSet, basename="list-perfil")

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
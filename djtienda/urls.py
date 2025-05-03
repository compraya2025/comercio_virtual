
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view # type: ignore
from drf_yasg import openapi # type: ignore
from django.contrib import admin
from django.urls import path, re_path, include

schema_view = get_schema_view(
   openapi.Info(
      title="COMERCIO VIRTUAL API REST",
      default_version='v1',
      description="comercio virtual compraya",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    #
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #
    re_path('api/v1/', include('applications.users.urls')),
    re_path('api/v1/', include('applications.profiles.urls')),
    re_path('api/v1/', include('applications.country.urls')),
    re_path('api/v1/', include('applications.department.urls')),
    re_path('api/v1/', include('applications.city.urls')),
    re_path('api/v1/', include('applications.custom.urls')),
    re_path('api/v1/', include('applications.store.urls')),
    re_path('api/v1/', include('applications.tax.urls')),
    re_path('api/v1/', include('applications.category.urls')),
    re_path('api/v1/', include('applications.product.urls')),
    re_path('api/v1/', include('applications.budget.urls')),
    re_path('api/v1/', include('applications.audit.urls')),
]

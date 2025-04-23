from  rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView) # type: ignore
#
from rest_framework.routers import DefaultRouter
#
from django.urls  import path, include
from . import views
#
router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename="users")
router.register(r'users-report', views.UserReportViewSet, basename="users-report")
router.register(r'users-filter', views.UserFilterViewSet, basename="users-filter")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
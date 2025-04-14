from  rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView) # type: ignore
#
from rest_framework.routers import DefaultRouter
#
from django.urls  import path, include
from . import views
#
router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename="users")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
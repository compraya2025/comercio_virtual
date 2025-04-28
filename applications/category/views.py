#
from rest_framework import viewsets
#
from rest_framework import status
from rest_framework.response import Response
#
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#
from .serializers import CategorySerializer
from .models import Categories
from .filters import CategoryFilters

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()
    filterset_class = CategoryFilters
    #
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated,IsAdminUser]

class CategoryReportViewSet(viewsets.ModelViewSet):
    #GET /api/v1/category-report/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD

    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = Categories.objects.all().order_by('created')
        params = self.request.query_params
        start = params.get('start_date')
        end   = params.get('end_date')

        if start:
            qs = qs.filter(created__date__gte=start)
        if end:
            qs = qs.filter(created__date__lte=end)
        return qs
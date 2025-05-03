from rest_framework import viewsets
from .serializers import AuditSerializer
from .models import Audit

# Create your views here.
class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer

    
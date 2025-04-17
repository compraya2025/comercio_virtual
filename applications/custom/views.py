from rest_framework import viewsets
#
from rest_framework import status
from rest_framework.response import Response

from .serializers import CustomerSerializer
from .models import Custom


# Create your views here.
class CustomersViewSet(viewsets.ModelViewSet):
    # queryset = Custom.objects.select_related('profile').all()
    queryset = Custom.objects.filter(profile__user__is_suscription=True)
    serializer_class = CustomerSerializer
    
    def get_queryset(self):
        queryset = Custom.objects.all()
        
        is_suscription = self.request.query_params.get('is_suscription')
        
        if is_suscription is not None:
            if is_suscription.lower() == 'true':
                queryset = queryset.filter(profile__user__is_suscription=True)
            elif is_suscription.lower() == 'false':
                queryset = queryset.filter(profile__user__is_suscription=False)
        
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, pk=None):
        if request.method == 'PUT':
            return Response({'error': 'Método PUT no permitido. Usa PATCH.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
         
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, pk=None, **kwargs):        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Registro actualizado correctamente."}, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'Registro eliminado existoso!'},status=status.HTTP_204_NO_CONTENT)

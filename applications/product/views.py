from rest_framework import viewsets
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
#
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ProductSerializer
from applications.audit.models import Audit
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

         # Obtener la instancia del producto creado
        product_instance = Product.objects.get(pk=serializer.data['id'])
        Audit.objects.create(producto=product_instance, usuario=self.request.user, accion="INSERT")
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
        Audit.objects.create(producto=serializer, usuario=self.request.user, accion="UPDATE")
        return Response({"message": "Registro actualizado correctamente."}, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        Audit.objects.create(producto=instance, usuario=self.request.user, accion="DELETE")
        return Response({'Registro eliminado existoso!'},status=status.HTTP_204_NO_CONTENT)


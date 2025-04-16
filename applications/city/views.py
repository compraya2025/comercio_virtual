#
from rest_framework import viewsets
#
from rest_framework import status
from rest_framework.response import Response
#
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#
from .serializers import CitySerializer
from .models import Cities

# Create your views here.
class CityViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer
    #
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated,IsAdminUser]

    def list(selt, request,  *args, **kwargs):
        queryset = Cities.objects.all()

        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
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
        return Response({"message": "Registro actualizado correctamente."}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'Registro eliminado existoso!'},status=status.HTTP_204_NO_CONTENT)
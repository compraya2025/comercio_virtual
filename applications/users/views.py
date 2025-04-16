from rest_framework import viewsets
from rest_framework.views import APIView
#
from rest_framework.authtoken.models import Token
#
from rest_framework.response import Response
#
from rest_framework import status
#
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#
from .models import User
from .serializers import UserSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated,IsAdminUser]

    def list(selt, request,  *args, **kwargs):
        queryset = User.objects.all()

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        # Obtiene el serializer con los datos de la request
        serializer = self.get_serializer(data=request.data)
        # Valida los datos o lanza excepción si hay errores
        serializer.is_valid(raise_exception=True)
        # Crea el usuario utilizando el método perform_create definido
        self.perform_create(serializer)
        # Obtiene los headers adecuados, por ejemplo, la URL del nuevo recurso
        headers = self.get_success_headers(serializer.data)
        # Retorna la respuesta con datos creados y el status HTTP 201
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        # Obtiene la instancia actual del usuario a actualizar
        instance = self.get_object()

        # Si queremos permitir actualizaciones parciales (PATCH) se identifica aquí
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        # Valida los datos
        serializer.is_valid(raise_exception=True)
        
        # Realiza la actualización del objeto
        self.perform_update(serializer)
        
        # Retorna la respuesta con los datos actualizados
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        # Obtiene la instancia del usuario a través del pk
        instance = self.get_object()
        # Serializa la instancia
        serializer = self.get_serializer(instance)
        # Retorna la respuesta con los datos serializados y un status 200 OK
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

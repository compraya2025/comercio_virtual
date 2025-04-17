from rest_framework import viewsets
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
#

from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ProfileSerializer, ProfilesSerializer
from applications.profiles.models import Profile
#
from applications.country.models    import Country
from applications.department.models import Departments
from applications.city.models       import Cities

#from applications.profiles.filters import ProfileFilter

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #filterset_class = ProfileFilter

      #
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated,IsAdminUser]

    def list(selt, request,  *args, **kwargs):
        queryset = Profile.objects.all()

        serializer = ProfileSerializer(queryset, many=True)
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

class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related('country','department','city').all()
    serializer_class = ProfilesSerializer

    def list(self, request, *args, **kwargs):
        perfiles_data = self.get_serializer(self.get_queryset(), many=True).data

        country    = list(Country.objects.values('id', 'name'))
        department = list(Departments.objects.values('id', 'name'))
        city       = list(Cities.objects.values('id', 'name'))

        for perfil in perfiles_data:
            perfil['country']    = country
            perfil['department'] = department
            perfil['city']       = city

        return Response(perfiles_data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        perfil = self.get_serializer(self.get_object()).data

        country    = list(Country.objects.values('id','name'))
        department = list(Departments.objects.values('id','name'))
        city       = list(Cities.objects.values('id','name'))

        perfil['country']    = country
        perfil['department'] = department
        perfil['city']       = city

        return Response(perfil, status=status.HTTP_200_OK)

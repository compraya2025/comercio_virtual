from rest_framework import viewsets
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ProfileSerializer
from applications.profiles.models import Profile

#from applications.profiles.filters import ProfileFilter

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

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
    
class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #filterset_class = ProfileFilter


class ProfileCreateView(CreateAPIView):
    serializer_class = ProfileSerializer
    
   # def perform_create(self, serializer):        
   #     serializer.save(user=self.request.user)

class ProfileUpdateView(UpdateAPIView):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'pk'

    def update(self, request,*args,**kwargs):
        if self.request.method == 'PUT':
            return Response({'error':'metodo PUT no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update( request,*args,**kwargs)
    #patch
    def perform_update(self, serializer):
        serializer.validated_data['full_name'] = serializer.validated_data['full_name']
        serializer.validated_data['user'] = serializer.validated_data['user']
        serializer.validated_data['photo_profile'] = serializer.validated_data['photo_profile']
        serializer.save()

class ProfileDeleteView(DestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'pk'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'Registro eliminado existoso!'},status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        print('--eliminar')
        return super().perform_destroy(instance) 
from rest_framework import serializers

from .models import Profile
from applications.country.models import Country
from applications.department.models import Departments
from applications.city.models import Cities

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'photo_profile',
            'full_name',
            'user',
            'age_profile',
            'neighborhood',
            'ruc_profile',
            'phone_profile',
            'birth_date',
            'address',
            'country',
            'department',
            'city',
            'created',
            'modified',
        )
    
class ProfileCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')
        ref_name = 'ProfileCountry'  

class ProfileDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'name') 
        ref_name = 'ProfileDepartment'  

class ProfileCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ('id', 'name')
        ref_name = 'ProfileCitySerializer'

class ProfilesSerializer(serializers.ModelSerializer):
     #para  lectura
     country    = ProfileCountrySerializer(read_only=True)
     department = ProfileDepartmentSerializer(read_only=True)
     city       = ProfileCitySerializer(read_only=True)

     # claves foráneas para escritura
     country_id    = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(),    source='country',    write_only=True)
     department_id = serializers.PrimaryKeyRelatedField(queryset=Departments.objects.all(), source='department', write_only=True)
     city_id       = serializers.PrimaryKeyRelatedField(queryset=Cities.objects.all(),source='city', write_only=True)

     class Meta:
        model = Profile
        fields = (
            'id',
            'photo_profile',
            'full_name',
            'user',
            'age_profile',
            'neighborhood',
            'ruc_profile',
            'phone_profile',
            'birth_date',
            'address',
            'country',
            'country_id',
            'department',
            'department_id',
            'city',
            'city_id',
            'created',
            'modified',
        )
        ref_name = 'ProfilesWithNestedPlaces' 
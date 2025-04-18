from rest_framework import serializers
#
from applications.profiles.models import Profile
from .models import Custom
from applications.department.models import Departments
from applications.city.models import Cities

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id','name')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ('id','name')

class ProfileSerializer(serializers.ModelSerializer):
     #para  lectura
    department = DepartmentSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    class Meta:
        model = Profile
        fields = (
            'id',
            'full_name',
            'age_profile',
            'neighborhood',
            'ruc_profile',
            'phone_profile',
            'address',
            'department',
            'city',
        )

class CustomerSerializer(serializers.ModelSerializer):
     #para  lectura
     profile = ProfileSerializer(read_only=True)

     # claves foráneas para escritura
     profile_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(),source='profile',write_only=True)
     class Meta:
         model = Custom
         fields = ('id','profile','profile_id','created','modified')
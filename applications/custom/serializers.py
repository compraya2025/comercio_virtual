from rest_framework import serializers
#
from applications.profiles.models import Profile
from .models import Custom

class ProfileSerializer(serializers.ModelSerializer):
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
        )

class CustomerSerializer(serializers.ModelSerializer):
     #para  lectura
     profile = ProfileSerializer(read_only=True)

     # claves foráneas para escritura
     profile_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(),source='profile',write_only=True)
     class Meta:
         model = Custom
         fields = ('id','profile','profile_id','created','modified')
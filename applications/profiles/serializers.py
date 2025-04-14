from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'photo_profile',
            'full_name',
            'user',
            'age_profile',
            'phone_profile',
            'birth_date',
            'address',
            'created',
            'modified',
        )
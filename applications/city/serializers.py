from rest_framework import serializers

from .models import Cities

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = (
            'id',
            'name',
            'department',
            'created',
            'modified'
        )
    ref_name = 'MainCitySerializer'
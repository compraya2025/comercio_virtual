from rest_framework import serializers

from .models import Departments

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id','name','country','created','modified')
        ref_name = 'MainDepartmentSerializer'
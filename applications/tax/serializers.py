from rest_framework import serializers

from .models import Taxes

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxes
        fields = ('id','name','percentage','created','modified')
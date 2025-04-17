from rest_framework import serializers

from .models import Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id','name_store', 'address','phone_store', 'image_baner', 'image_horizontal','image_vertical','created','modified')

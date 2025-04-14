from rest_framework import serializers
#
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer # type: ignore

from .models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    repeat_password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ['id','name','last_name','username','email','password','repeat_password','created','modified']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('repeat_password')  
        user = User.objects.create_user(
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id','name','last_name','username','email','password','repeat_password','created','modified') 
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Credenciales inválidas.")
        if not user.is_active:
            raise serializers.ValidationError("Cuenta inactiva.")
        return {'user': user}
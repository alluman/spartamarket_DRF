from .models import User
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birthday', 'gender', 'introduction']
        extra_kwargs = {"password": {"write_only":True}}

class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'nickname', 'birthday', 'gender', 'introduction']
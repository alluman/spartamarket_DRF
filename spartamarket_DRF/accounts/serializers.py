from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birthday', 'gender', 'introduction']
        extra_kwargs = {"password": {"write_only":True}}
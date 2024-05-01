from rest_framework import serializers
from .models import Product
from accounts.models import User

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'created_at', 'view', 'price', 'author']
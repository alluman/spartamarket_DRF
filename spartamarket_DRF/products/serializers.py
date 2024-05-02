from rest_framework import serializers
from .models import Product
from accounts.models import User

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # hashtags = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'created_at', 'view', 'author', 'like_user', 'price', 'image'] #, 'hashtags'
        read_only_fields = ['author', 'like_user']
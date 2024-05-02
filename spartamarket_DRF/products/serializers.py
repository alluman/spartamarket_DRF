from rest_framework import serializers
from .models import Product, Hashtag
from accounts.models import User

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    hashtags = HashtagSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'created_at', 'view', 'author', 'like_user', 'price', 'image', 'hashtags']
        read_only_fields = ['author', 'like_user']

    def create(self, validated_data):
        hashtags_data = validated_data.pop('hashtags', [])
        product = Product.objects.create(**validated_data)
        for hashtag_data in hashtags_data:
            hashtag, _ = Hashtag.objects.get_or_create(name=hashtag_data['name'])
            product.hashtags.add(hashtag)
        return product

    def get_tag_name(self, obj):
        return [tag.name for tag in obj.tag_set.all()]
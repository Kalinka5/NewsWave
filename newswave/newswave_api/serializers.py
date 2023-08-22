from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from .models import News, Category, Image


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True, source='image_set')

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'category', 'images']

    def create(self, validated_data):
        images_data = self.context.get('request').data.getlist('images')  # Get the list of image data
        
        news_instance = News.objects.create(**validated_data)
        
        for image_data in images_data:
            Image.objects.create(news_name=news_instance, image=image_data)

        return news_instance

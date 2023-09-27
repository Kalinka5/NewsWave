from rest_framework import serializers
from django.utils.text import slugify

from django.contrib.auth.models import User

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


class CurrentUserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups']

    def get_groups(self, obj):
        groups = obj.groups.all()
        return [group.name for group in groups]


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        # Generate the slug from the title before creating the category
        title = validated_data.get('title')
        validated_data['slug'] = slugify(title)
        
        # Call the parent class's create method to actually create the category
        category = super(CategorySerializer, self).create(validated_data)
        
        return category


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
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        
        # Save the updated instance
        instance.save()

        # Update images
        images_data = self.context['request'].data.getlist('images')

        # Handle images for PUT request (replace all images)
        if self.context.get('request').method == 'PUT':
            instance.image_set.all().delete()  # Remove existing images

        for image_data in images_data:
            Image.objects.create(news_name=instance, image=image_data)

        return instance

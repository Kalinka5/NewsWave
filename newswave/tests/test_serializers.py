from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from newswave_api.serializers import (
    RegisterSerializer,
    UserSerializer,
    CurrentUserSerializer,
    CategorySerializer,
    ImageSerializer,
    NewsSerializer,
)
from newswave_api.models import Category, News
import os


class SerializerTests(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@gmail.com',
            'first_name': 'Test',
            'last_name': 'User',
        }
        self.user = User.objects.create_user(**self.user_data)
        # Create some initial test data
        self.category = Category.objects.create(title='Test Category')
        self.news = News.objects.create(
            title='Test News',
            description='This is a test news article.',
            category=self.category
        )

    def test_valid_register_serializer(self):
        new_user = {
            'username': 'newuser',
            'password': 'testpassword',
            'email': 'newtestuser@gmail.com',
            'first_name': 'Dan',
            'last_name': 'Kaliny',
        }
        serializer = RegisterSerializer(data=new_user)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, new_user['username'])

    def test_user_serializer(self):
        serializer = UserSerializer(instance=self.user)
        self.assertEqual(serializer.data['username'], self.user.username)
    
    def test_current_user_serializer(self):
        serializer = CurrentUserSerializer(instance=self.user)
        self.assertEqual(serializer.data['username'], self.user.username)

    def test_category_serializer(self):
        category_data = {'title': 'Test Category'}
        serializer = CategorySerializer(data=category_data)
        self.assertTrue(serializer.is_valid())
        category = serializer.save()
        self.assertEqual(category.slug, 'test-category')

    def test_image_jpg_serializer(self):
        root_folder = os.getcwd()
        image_path = os.path.join(root_folder, 'tests', 'test_images', 'jpg_image.jpg')
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        image = SimpleUploadedFile("jpg_image.jpg", image_data, content_type="image/jpeg")
        image_data = {'image': image, 'news_name': self.news.pk}
        serializer = ImageSerializer(data=image_data)
        self.assertTrue(serializer.is_valid())

    def test_image_png_serializer(self):
        root_folder = os.getcwd()
        image_path = os.path.join(root_folder, 'tests', 'test_images', 'png_image.png')
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        image = SimpleUploadedFile("png_image.png", image_data, content_type="image/png")
        image_data = {'image': image, 'news_name': self.news.pk}
        serializer = ImageSerializer(data=image_data)
        self.assertTrue(serializer.is_valid())

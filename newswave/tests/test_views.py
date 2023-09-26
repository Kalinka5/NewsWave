from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group
from newswave_api.models import Category, News
from newswave_api.serializers import CategorySerializer, NewsSerializer

class NewsTests(TestCase):
    def setUp(self):
        # Create a test user and assign them to the 'Manager' group for permissions
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.manager_group = Group.objects.create(name='Manager')
        self.user.groups.add(self.manager_group)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create some initial test data
        self.category = Category.objects.create(title='Test Category')
        self.news = News.objects.create(
            title='Test News',
            description='This is a test news article.',
            category=self.category
        )

    def test_list_categories(self):
        url = reverse('categories')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_categories = CategorySerializer(Category.objects.all(), many=True)
        self.assertEqual(response.data, serialized_categories.data)

    def test_create_category(self):
        url = reverse('categories')
        data = {
            'slug': 'new_category',
            'title': 'New Category',
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)  # Check that a new category was created

    def test_retrieve_category(self):
        url = reverse('single_category', args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_category = CategorySerializer(self.category)
        self.assertEqual(response.data, serialized_category.data)

    def test_list_news(self):
        url = reverse('news')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_news = NewsSerializer(News.objects.all(), many=True)
        self.assertEqual(response.data, serialized_news.data)

    # def test_create_news(self):
    #     url = reverse('news')
    #     image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
    #     data = {
    #         'title': 'New News',
    #         'description': 'This is a new test news article.',
    #         'category': self.category.id,
    #         'images': [image_file]
    #     }
    #     response = self.client.post(url, data, format='multipart')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(News.objects.count(), 2)  # Check that a new news article was created

    #     # Check that the created news entry has the correct image associated with it
    #     created_news = News.objects.latest('id')
    #     self.assertEqual(created_news.images.count(), 1)

    def test_retrieve_news(self):
        url = reverse('single_news', args=[self.news.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_news = NewsSerializer(self.news)
        self.assertEqual(response.data, serialized_news.data)
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group
from newswave_api.models import Category, News
from newswave_api.serializers import CategorySerializer, NewsSerializer

class TestViews(TestCase):
    def setUp(self):
        # Create a test user and assign them to the 'Manager' group for permissions
        self.user = User.objects.create_user(username='testuser1', password='testpassword1')
        self.manager_group = Group.objects.create(name='Manager')
        self.user.groups.add(self.manager_group)
        self.manager_client = APIClient()
        self.manager_client.force_authenticate(user=self.user)

        # Create an ordinary user with no permissions
        self.user = User.objects.create_user(username='testuser2', password='testpassword2')
        self.ordinary_client = APIClient()
        self.ordinary_client.force_authenticate(user=self.user)

        # Create some initial test data
        self.category = Category.objects.create(title='Test Category')
        self.news = News.objects.create(
            title='Test News',
            description='This is a test news article.',
            category=self.category
        )

    def test_register_user_POST(self):
        url = reverse('register_new_user')
        data = {
            'username': 'new_user',
            'password': 'new_password',
            'email': 'newemail123@gmail.com',
            'first_name': 'John',
            'last_name': 'Week',
            }
        response = self.ordinary_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['id'], 3)
        self.assertEqual(response.data['user']['username'], 'new_user')
        self.assertEqual(response.data['user']['email'], 'newemail123@gmail.com')
        self.assertEqual(response.data['user']['first_name'], 'John')
        self.assertEqual(response.data['user']['last_name'], 'Week')

    def test_current_user_manager_GET(self):
        url = reverse('current_user')
        response = self.manager_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser1')
        self.assertEqual(response.data['first_name'], '')
        self.assertEqual(response.data['last_name'], '')
        self.assertEqual(response.data['email'], '')
        self.assertEqual(response.data['groups'], ['Manager'])
    
    def test_current_user_ordinary_GET(self):
        url = reverse('current_user')
        response = self.ordinary_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser2')
        self.assertEqual(response.data['first_name'], '')
        self.assertEqual(response.data['last_name'], '')
        self.assertEqual(response.data['email'], '')
        self.assertEqual(response.data['groups'], [])

    def test_list_categories_manager_GET(self):
        url = reverse('categories')
        response = self.manager_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_categories = CategorySerializer(Category.objects.all(), many=True)
        self.assertEqual(response.data, serialized_categories.data)

    def test_list_categories_ordinary_GET(self):
        url = reverse('categories')
        response = self.ordinary_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_categories = CategorySerializer(Category.objects.all(), many=True)
        self.assertEqual(response.data, serialized_categories.data)

    def test_create_category_manager_POST(self):
        url = reverse('categories')
        data = {
            'slug': 'new_category',
            'title': 'New Category',
            }
        response = self.manager_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)  # Check that a new category was created

    def test_create_category_ordinary_POST(self):
        url = reverse('categories')
        data = {
            'slug': 'new_category',
            'title': 'New Category',
            }
        response = self.ordinary_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_category_manager_GET(self):
        url = reverse('single_category', args=[self.category.id])
        response = self.manager_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_category = CategorySerializer(self.category)
        self.assertEqual(response.data, serialized_category.data)

    def test_retrieve_category_ordinary_GET(self):
        url = reverse('single_category', args=[self.category.id])
        response = self.ordinary_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_category = CategorySerializer(self.category)
        self.assertEqual(response.data, serialized_category.data)

    def test_list_news_manager_GET(self):
        url = reverse('news')
        response = self.manager_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_news = NewsSerializer(News.objects.all(), many=True)
        self.assertEqual(response.data, serialized_news.data)

    def test_list_news_ordinary_GET(self):
        url = reverse('news')
        response = self.ordinary_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_news = NewsSerializer(News.objects.all(), many=True)
        self.assertEqual(response.data, serialized_news.data)

    def test_create_news_manager_POST(self):
        url = reverse('news')
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        data = {
            'title': 'New News',
            'description': 'This is a new test news article.',
            'category': self.category.id,
            'images': [image_file]
        }
        response = self.manager_client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 2)  # Check that a new news article was created

    def test_create_news_ordinary_POST(self):
        url = reverse('news')
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        data = {
            'title': 'New News',
            'description': 'This is a new test news article.',
            'category': self.category.id,
            'images': [image_file]
        }
        response = self.ordinary_client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_news_manager_GET(self):
        url = reverse('single_news', args=[self.news.id])
        response = self.manager_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_news = NewsSerializer(self.news)
        self.assertEqual(response.data, serialized_news.data)

    def test_retrieve_news_ordinary_GET(self):
        url = reverse('single_news', args=[self.news.id])
        response = self.ordinary_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_news = NewsSerializer(self.news)
        self.assertEqual(response.data, serialized_news.data)

    def test_update_full_single_news_manager_PUT(self):
        url = reverse('single_news', args=[self.news.id])
        image_file = SimpleUploadedFile("test_update_image.jpg", b"file_content", content_type="image/jpeg")
        data = {
            'title': 'Updated News',
            'description': 'This is an updated test news article.',
            'category': self.category.id,
            'images': [image_file]
        }
        response = self.manager_client.put(url, data, format='multipart')
        news = News.objects.get(id=self.news.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(news.title, 'Updated News')
        self.assertEqual(news.description, 'This is an updated test news article.')

    def test_update_full_single_news_ordinary_PUT(self):
        url = reverse('single_news', args=[self.news.id])
        image_file = SimpleUploadedFile("test_update_image.jpg", b"file_content", content_type="image/jpeg")
        data = {
            'title': 'NOT updated News',
            'description': 'This is NOT an updated test news article.',
            'category': self.category.id,
            'images': [image_file]
        }
        response = self.ordinary_client.put(url, data, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_part_of_single_news_manager_PATCH(self):
        url = reverse('single_news', args=[self.news.id])
        image_file = SimpleUploadedFile("test_update_image1.jpg", b"file_content", content_type="image/jpeg")
        data1 = {
            'images': [image_file]
        }
        
        response = self.manager_client.patch(url, data1, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['images']), 1)

    def test_update_part_of_single_news_ordinary_PATCH(self):
        url = reverse('single_news', args=[self.news.id])
        image_file = SimpleUploadedFile("test_update_image1.jpg", b"file_content", content_type="image/jpeg")
        data1 = {
            'images': [image_file]
        }
        
        response = self.ordinary_client.patch(url, data1, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_single_news_manager_DELETE(self):
        url = reverse('single_news', args=[self.news.id])
        response = self.manager_client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_single_news_ordinary_DELETE(self):
        url = reverse('single_news', args=[self.news.id])
        response = self.ordinary_client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

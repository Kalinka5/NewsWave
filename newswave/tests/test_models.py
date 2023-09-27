from django.test import TestCase
from newswave_api.models import Category, News, Image

class TestModels(TestCase):
    def setUp(self):
        self.category = Category.objects.create(slug="test-category", title="Test Category")
        self.news = News.objects.create(title="Test News", description="This is a test news", category=self.category)
        self.image = Image.objects.create(image="test-image.jpg", news_name=self.news)

    def test_category_slug(self):
        self.assertEqual(self.category.slug, "test-category")

    def test_news_description(self):
        self.assertEquals(self.news.description, "This is a test news")

    def test_count_news_in_current_category(self):
        self.news = News.objects.create(title="Test News 2", description="This is a test news 2", category=self.category)
        self.assertEqual(self.category.news_set.count(), 2)

    def test_count_images_in_current_news(self):
        Image.objects.create(image="test-image2.jpg", news_name=self.news)
        Image.objects.create(image="test-image3.jpg", news_name=self.news)
        self.assertEqual(self.news.image_set.count(), 3)

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_news_str(self):
        self.assertEqual(str(self.news), "Test News")

    def test_image_str(self):
        self.assertEqual(str(self.image), "test-image.jpg")

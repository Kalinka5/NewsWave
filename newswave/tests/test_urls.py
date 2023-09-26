from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from newswave_api.views import NewsListView, CategoriesListView, RegisterApi, NewsDetailView, single_category, current_user


class TestUrls(SimpleTestCase):

    def test_get_token_url_resolves(self):
        url = reverse('get_token')
        self.assertEquals(resolve(url).func.view_class, TokenObtainPairView)

    def test_refresh_token_url_resolves(self):
        url = reverse('refresh_token')
        self.assertEquals(resolve(url).func.view_class, TokenRefreshView)

    def test_register_new_user_url_resolves(self):
        url = reverse('register_new_user')
        self.assertEquals(resolve(url).func.view_class, RegisterApi)

    def test_news_categories_url_resolves(self):
        url = reverse('categories')
        self.assertEquals(resolve(url).func.view_class, CategoriesListView)

    def test_single_category_url_resolves(self):
        url = reverse('single_category', args=[1])
        self.assertEquals(resolve(url).func, single_category)

    def test_news_list_url_resolves(self):
        url = reverse('news')
        self.assertEquals(resolve(url).func.view_class, NewsListView)

    def test_news_detail_url_resolves(self):
        url = reverse('single_news', args=[1])
        self.assertEquals(resolve(url).func.view_class, NewsDetailView)

    def test_user_detail_url_resolves(self):
        url = reverse('current_user')
        self.assertEquals(resolve(url).func, current_user)

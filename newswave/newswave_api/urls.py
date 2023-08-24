from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import NewsListView, CategoriesListView, RegisterApi, NewsDetailView, single_category, current_user


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('register', RegisterApi.as_view()),
    path('categories', CategoriesListView.as_view(), name='categories'),
    path('categories/<int:pk>', single_category, name='single_category'),
    path('news', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='single_news'),
    path('current-user/', current_user, name='current-user'),
]
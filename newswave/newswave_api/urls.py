from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import news, categories, single_category, single_news, RegisterApi


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('register', RegisterApi.as_view()),
    path('categories', categories, name='categories'),
    path('categories/<int:pk>', single_category, name='single_category'),
    path('news', news, name='news'),
    path('news/<int:pk>', single_news, name='single_news'),
]
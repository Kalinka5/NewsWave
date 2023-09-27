from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import News, Category
from .serializers import NewsSerializer, CategorySerializer, RegisterSerializer, UserSerializer, CurrentUserSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Add throttling

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([AnonRateThrottle, UserRateThrottle])
def current_user(request):
    user = request.user
    serializer = CurrentUserSerializer(user)
    return Response(serializer.data)


class CategoriesListView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Add throttling

    def get(self, request):
        items = Category.objects.all()
        serialized_category = CategorySerializer(items, many=True)

        return Response(serialized_category.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if request.user.groups.filter(name='Manager').exists():
            serialized_category = CategorySerializer(data=request.data)
            serialized_category.is_valid(raise_exception=True)
            serialized_category.save()
            return Response(serialized_category.data, status.HTTP_201_CREATED)
        else:
            return Response({"message": "You do not have the necessary permissions to access it!"}, status=status.HTTP_403_FORBIDDEN)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([AnonRateThrottle, UserRateThrottle])
def single_category(request, pk):
    item = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(item)
    return Response(serialized_category.data, status=status.HTTP_200_OK)


class NewsListView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Add throttling

    def get(self, request):
        items = News.objects.prefetch_related('category', 'image_set').all()

        # Filtering
        category_name = request.query_params.get('category')
        if category_name:
            items = items.filter(category__title=category_name)

        # Pagination
        perpage = request.query_params.get('perpage', default=3)
        page = request.query_params.get('page', default=1)
        paginator = Paginator(items, per_page=perpage)

        try:
            items = paginator.page(number=page)
        except EmptyPage:
            return Response([], status=status.HTTP_204_NO_CONTENT)

        serialized_item = NewsSerializer(items, many=True)
        return Response(serialized_item.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.groups.filter(name='Manager').exists():
            return Response({"message": "You do not have the necessary permissions to access it!"}, status=status.HTTP_403_FORBIDDEN)
        
        serialized_item = NewsSerializer(data=request.data, context={'request': request})
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


class NewsDetailView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Add throttling

    def get_object(self, pk):
        return get_object_or_404(News, pk=pk)

    def get(self, request, pk):
        news_instance = self.get_object(pk)
        serializer = NewsSerializer(news_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        if not request.user.groups.filter(name='Manager').exists():
            return Response({"message": "You do not have the necessary permissions to access it!"}, status=status.HTTP_403_FORBIDDEN)

        news_item = News.objects.get(pk=pk)
        serializer = NewsSerializer(news_item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        if not request.user.groups.filter(name='Manager').exists():
            return Response({"message": "You do not have the necessary permissions to access it!"}, status=status.HTTP_403_FORBIDDEN)

        news_item = News.objects.get(pk=pk)
        serializer = NewsSerializer(news_item, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not request.user.groups.filter(name='Manager').exists():
            return Response({"message": "You do not have the necessary permissions to access it!"}, status=status.HTTP_403_FORBIDDEN)
        
        news_instance = self.get_object(pk)
        news_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
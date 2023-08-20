from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage

from rest_framework import status, generics, permissions, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import News, Category
from .serializers import NewsSerializer, CategorySerializer, RegisterSerializer, UserSerializer


#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def categories(request):
    items = Category.objects.all()
    serialized_category = CategorySerializer(items, many=True)

    if request.method == 'GET':
        return Response(serialized_category.data, status=status.HTTP_200_OK)
    
    if request.user.groups.filter(name='Manager').exists():
        if request.method == 'POST':
            serialized_category = CategorySerializer(data=request.data)
            serialized_category.is_valid(raise_exception=True)
            serialized_category.save()
            return Response(serialized_category.data, status.HTTP_201_CREATED)
    else:
        return Response({"message": "You do not have the necessary permissions to access it!"}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def news(request):
    items = News.objects.prefetch_related('category', 'image_set').all()

    # filtering
    category_name = request.query_params.get('category')
    if category_name:
        items = items.filter(category__title=category_name)

    # pagination
    perpage = request.query_params.get('perpage', default=3)
    page = request.query_params.get('page', default=1)
    paginator = Paginator(items, per_page=perpage)

    try:
        items = paginator.page(number=page)
    except EmptyPage:
        return Response([], status=status.HTTP_204_NO_CONTENT)

    serialized_item = NewsSerializer(items, many=True)

    if request.method == 'POST':

        if request.user.groups.filter(name='Manager').exists():
            serialized_item = NewsSerializer(data=request.data, context={'request': request})
            serialized_item.is_valid(raise_exception=True)
            serialized_item.save()
            return Response(serialized_item.data, status.HTTP_201_CREATED)
        
        else:
            return Response({"message": "You do not have the necessary permissions to access it!"}, status=status.HTTP_403_FORBIDDEN)
    
    return Response(serialized_item.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def single_news(request, pk):
    item = get_object_or_404(News, pk=pk)
    if request.method == 'GET':
        serialized_item = NewsSerializer(item)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    
    if request.user.groups.filter(name='Manager').exists():

        if request.method == 'PUT':
            serializer = NewsSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'PATCH':
            serializer = NewsSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"message": "You do not have the necessary permissions to access it!"}, status=status.HTTP_403_FORBIDDEN)
    
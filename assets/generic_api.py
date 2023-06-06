from rest_framework import generics, pagination
from .models import AssetsCategory, Assets
from .serializers import AssetsCategorySerializer, AssetsListSerializer


class CustomPagination(pagination.PageNumberPagination):
    """
    自定义分页类
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AssetsCategoryAPIView(generics.ListCreateAPIView):
    queryset = AssetsCategory.objects.all()
    serializer_class = AssetsCategorySerializer
    pagination_class = CustomPagination


class AssetsCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssetsCategory.objects.all()
    serializer_class = AssetsCategorySerializer


class AssetsAPIView(generics.ListCreateAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsListSerializer
    pagination_class = CustomPagination


class AssetsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsListSerializer

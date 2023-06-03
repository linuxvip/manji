from rest_framework import viewsets, pagination
from .models import AssetsCategory, Assets
from .serializers import AssetsCategorySerializer, AssetsSerializer
from .renderers import CustomJSONRenderer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per_page'
    max_page_size = 100


class AssetsCategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetsCategory.objects.all()
    serializer_class = AssetsCategorySerializer
    renderer_classes = [CustomJSONRenderer]


class AssetsViewSet(viewsets.ViewSet):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer
    pagination_class = CustomPagination
    renderer_classes = [CustomJSONRenderer]


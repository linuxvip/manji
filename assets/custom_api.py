from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework import status

from .models import AssetsCategory, Assets
from .serializers import AssetsCategorySerializer, AssetsListSerializer, AssetsUpdateSerializer


class CustomPagination(pagination.PageNumberPagination):
    """
    CustomPagination是一个自定义的分页器类，继承自DRF的pagination.PageNumberPagination。
    在这个类中，我们定义了每页显示的记录数为10，可以通过查询参数per_page来指定每页的记录数，最大允许的每页记录数为100。
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AssetCategoryViewSet(viewsets.ModelViewSet):
    """
    资产分类视图集
    """
    queryset = AssetsCategory.objects.all()
    serializer_class = AssetsCategorySerializer


class AssetViewSet(viewsets.ModelViewSet):
    """
    资产管理视图集,自定义某个方法
    """
    queryset = Assets.objects.filter(is_delete=False)
    pagination_class = CustomPagination

    def get_serializer_class(self):
        """
        动态获取序列化器类
        """
        if self.request.method == "POST" or self.request.method == "PUT":
            serializer_class = AssetsUpdateSerializer
            return serializer_class
        else:
            serializer_class = AssetsListSerializer
            return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        asset = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(asset).data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        asset = serializer.save()
        return Response(self.get_serializer(asset).data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.is_delete = True
        instance.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)
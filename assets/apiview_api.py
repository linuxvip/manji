from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination
from .models import AssetsCategory, Assets
from .serializers import AssetsCategorySerializer, AssetsSerializer
from .renderers import CustomJSONRenderer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per_page'
    max_page_size = 100


class AssetsCategoryAPIView(APIView):
    def get(self, request):
        categories = AssetsCategory.objects.all()
        serializer = AssetsCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssetsCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetsCategoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return AssetsCategory.objects.get(pk=pk)
        except AssetsCategory.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            serializer = AssetsCategorySerializer(category)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            serializer = AssetsCategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            serializer = AssetsCategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AssetsAPIView(APIView):
    def get(self, request):
        assets = Assets.objects.all()
        serializer = AssetsSerializer(assets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetsDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Assets.objects.get(pk=pk)
        except Assets.DoesNotExist:
            return None

    def get(self, request, pk):
        asset = self.get_object(pk)
        if asset is not None:
            serializer = AssetsSerializer(asset)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        asset = self.get_object(pk)
        if asset is not None:
            serializer = AssetsSerializer(asset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        asset = self.get_object(pk)
        if asset is not None:
            serializer = AssetsSerializer(asset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        asset = self.get_object(pk)
        if asset is not None:
            asset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

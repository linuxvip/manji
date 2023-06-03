# 纯Django常用场景api示例
from django.urls import path
from .views import AssetsCategoryListView, AssetsListView

urlpatterns = [
    # 通过 .as_view() 方法将视图类转换为视图函数
    path('assets-categories/', AssetsCategoryListView.as_view(), name='assets_category_list'),
    path('assets/', AssetsListView.as_view(), name='assets_list'),
]


# from django.urls import include, path
# from rest_framework import routers
# from .api import AssetsCategoryViewSet, AssetsViewSet
#
# router = routers.DefaultRouter()
# router.register(r'assets-categories', AssetsCategoryViewSet)
# router.register(r'assets', AssetsViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]


# from django.urls import path
# from .generic_api import AssetsCategoryAPIView, AssetsCategoryDetailAPIView, AssetsAPIView, AssetsDetailAPIView
#
# urlpatterns = [
#     path('assets-categories/', AssetsCategoryAPIView.as_view(), name='assets-category-list'),
#     path('assets-categories/<int:pk>/', AssetsCategoryDetailAPIView.as_view(), name='assets-category-detail'),
#     path('assets/', AssetsAPIView.as_view(), name='assets-list'),
#     path('assets/<int:pk>/', AssetsDetailAPIView.as_view(), name='assets-detail'),
# ]


# from django.urls import path
# from .apiview_api import AssetsCategoryAPIView, AssetsCategoryDetailAPIView, AssetsAPIView, AssetsDetailAPIView
#
#
# urlpatterns = [
#     path('categories/', AssetsCategoryAPIView.as_view(), name='assets-category-list'),
#     path('categories/<int:pk>/', AssetsCategoryDetailAPIView.as_view(), name='assets-category-detail'),
#     path('assets/', AssetsAPIView.as_view(), name='assets-list'),
#     path('assets/<int:pk>/', AssetsDetailAPIView.as_view(), name='assets-detail'),
# ]
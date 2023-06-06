# # 纯Django常用场景api示例
# from django.urls import path
# from .views import AssetsCategoryListView, AssetsListView
#
# urlpatterns = [
#     # 通过 .as_view() 方法将视图类转换为视图函数
#     path('assets-categories/', AssetsCategoryListView.as_view(), name='assets_category_list'),
#     path('assets/', AssetsListView.as_view(), name='assets_list'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .custom_api import AssetCategoryViewSet, AssetViewSet

router = DefaultRouter()
router.register(r"assets", AssetViewSet, basename="assets")
router.register(r"category", AssetCategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]

# router是routers.DefaultRouter()的实例，它提供了自动生成URL路由的功能。
# router.register(r'assets', AssetsViewSet)将AssetsViewSet注册为名为"assets"的路由。这将生成以下URL路由：

# GET /assets/：获取资产列表
# POST /assets/：创建新的资产
# GET /assets/{pk}/：获取特定资产的详情
# PUT /assets/{pk}/：更新特定资产
# DELETE /assets/{pk}/：删除特定资产

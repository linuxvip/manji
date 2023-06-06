from rest_framework import serializers
from .models import Assets, AssetsCategory


class AssetsCategorySerializer(serializers.ModelSerializer):
    """
    资产分类模型序列化器
    """
    class Meta:
        model = AssetsCategory
        fields = ("id", "name", "parent_category", "created_by", "updated_by",
                  "date_created", "date_updated", "desc", "is_delete")


class AssetsListSerializer(serializers.ModelSerializer):
    """
    资产模型序列化器
    """
    assets_category = AssetsCategorySerializer(read_only=True)

    class Meta:
        model = Assets
        fields = (
            "id", "name", "address", "is_active", "assets_category",
            "created_by", "updated_by", "date_created", "date_updated", "desc", "is_delete",
        )
        read_only_fields = ("created_by", "updated_by", "date_created", "date_updated")


# {
#   "name": "test001"
#   "address": "192.168.100.10",
#   "assets_category": {
#       "name": "a",
#       "desc": "xxxx",
#       ………………
#   }
# }


class AssetsUpdateSerializer(serializers.ModelSerializer):
    """
    资产模型序列化器
    """

    class Meta:
        model = Assets
        fields = (
            "id", "name", "address", "is_active", "desc", "is_delete"
        )
        read_only_fields = ("created_by", "updated_by", "date_created", "date_updated")

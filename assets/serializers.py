from rest_framework import serializers
from .models import Assets, AssetsCategory


class AssetsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsCategory
        fields = '__all__'


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

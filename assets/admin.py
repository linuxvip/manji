from django.contrib import admin
from .models import AssetsCategory, Assets


@admin.register(AssetsCategory)
class AssetsCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent_category", "date_created")

    search_fields = ('id', 'name', )


@admin.register(Assets)
class AssetsAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "is_active", "assets_category", "date_created")
    search_fields = ('id', 'name', )

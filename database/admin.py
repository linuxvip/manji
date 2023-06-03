from django.contrib import admin
from .models import Database


@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'host', 'user', 'port', 'desc')
    search_fields = ('id', 'name', 'host', 'user')

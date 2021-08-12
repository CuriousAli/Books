from django.contrib import admin
from django.contrib.admin import ModelAdmin

from Service.models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns in the changelist
    list_display = ("title", "author", "publication_year")
    # Quick filters on the right
    list_filter = ("publication_year",)
    # Top search box (case-insensitive contains by default)
    search_fields = ("title", "author")
    # Nice-to-have defaults
    ordering = ("title",)
    list_per_page = 25

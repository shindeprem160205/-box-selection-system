from django.contrib import admin

from .models import Box


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "internal_length",
        "internal_width",
        "internal_height",
        "max_weight",
        "cost",
        "created_at",
    )
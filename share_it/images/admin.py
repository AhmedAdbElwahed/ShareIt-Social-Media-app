from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    """
    a class to represent the image model in the admin panel
    """
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
    raw_id_fields = ['user']

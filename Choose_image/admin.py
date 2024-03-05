from django.contrib import admin
from .models import Choose_image

class Choose_image_Admin(admin.ModelAdmin):
    list_display=['image']

admin.site.register(Choose_image,Choose_image_Admin)

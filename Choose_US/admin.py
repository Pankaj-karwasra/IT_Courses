from django.contrib import admin
from .models import Choose_US

class Us_Admin(admin.ModelAdmin):
    list_display=['title','description']

admin.site.register(Choose_US,Us_Admin)

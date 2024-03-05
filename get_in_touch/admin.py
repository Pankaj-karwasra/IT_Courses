from django.contrib import admin
from .models import get_in_touch

class get_in_touch_Admin(admin.ModelAdmin):
    list_display=['address','phone','email']

admin.site.register(get_in_touch,get_in_touch_Admin)

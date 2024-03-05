from django.contrib import admin
from .models import top_touch

class top_touch_Admin(admin.ModelAdmin):
    list_display=['phone','email']

admin.site.register(top_touch,top_touch_Admin)

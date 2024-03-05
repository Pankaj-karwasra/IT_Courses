from django.contrib import admin

from .models import Choose_US2

class Us_Admin2(admin.ModelAdmin):
    list_display=['title','description']

admin.site.register(Choose_US2,Us_Admin2)

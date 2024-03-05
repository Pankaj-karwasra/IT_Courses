from django.contrib import admin
from .models import Choose_US1

class Us_Admin1(admin.ModelAdmin):
    list_display=['title','description']

admin.site.register(Choose_US1,Us_Admin1)


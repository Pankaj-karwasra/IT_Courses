from django.contrib import admin
from.models import Recent

class RecentAdmin(admin.ModelAdmin):
    list_display=['image','title','name','rating','number']

admin.site.register(Recent,RecentAdmin)

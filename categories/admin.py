from django.contrib import admin
from.models import categories

class catAdmin(admin.ModelAdmin):
    list_display=['title','number']

admin.site.register(categories,catAdmin)

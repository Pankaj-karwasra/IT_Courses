from django.contrib import admin
from .models import aboutus

class aboutusAdmin(admin.ModelAdmin):
    list_display=['image','title','description','subjects','course','instructor','students']

admin.site.register(aboutus,aboutusAdmin)



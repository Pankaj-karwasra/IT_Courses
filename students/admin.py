from django.contrib import admin
from .models import students

class stAdmin(admin.ModelAdmin):
    list_display=['description','image','name','course']

admin.site.register(students,stAdmin)
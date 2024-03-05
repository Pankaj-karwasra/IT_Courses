from django.contrib import admin
from .models import course_details
# Register your models here.
class detailsAdmin(admin.ModelAdmin):
    list_display=['title','image','description','instructor','rating','lecture','duration','skill','language','price']

admin.site.register(course_details,detailsAdmin)
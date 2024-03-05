from django.contrib import admin
from .models import OurCourses

class CoursesAdmin(admin.ModelAdmin):
    list_display=['image','title','instructor','rating','num_reviws','views']

admin.site.register(OurCourses,CoursesAdmin)

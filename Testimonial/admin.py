from django.contrib import admin
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display=['description']

admin.site.register(Testimonial,TestimonialAdmin)
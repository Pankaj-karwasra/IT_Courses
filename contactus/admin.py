from django.contrib import admin
from .models import contactus

class contactusAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message']

admin.site.register(contactus,contactusAdmin)

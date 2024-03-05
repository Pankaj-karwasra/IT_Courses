from django.contrib import admin
from .models import Choose_TD

class TDAdmin(admin.ModelAdmin):
    list_display=['title','description']


admin.site.register(Choose_TD,TDAdmin)
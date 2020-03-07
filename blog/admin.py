from django.contrib import admin

# Register your models here.

from .models import post,laporan

admin.site.register(post)
admin.site.register(laporan)

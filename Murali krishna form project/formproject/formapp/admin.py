from django.contrib import admin
from .models import mode
# Register your models here.
@admin.register(mode)
class showmode(admin.ModelAdmin):
    list_display = ['name']
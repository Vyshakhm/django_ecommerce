from django.contrib import admin
from .models import *

# Register your models here.

class catadmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,catadmin)


class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','image']
    list_editable = ['stock','price','image']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,productadmin)
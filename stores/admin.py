from django.contrib import admin
from .models import MenuItem
from .models import Store

class MenuItemInline(admin.TabularInline):
    model=MenuItem
    extra=1
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display=['name', 'notes']
    inlines=[MenuItemInline]
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


# Register your models here.

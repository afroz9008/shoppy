from django.contrib import admin
from app.models import Products,Categories,SpecialItems


class AdminProducts(admin.ModelAdmin):
    list_display=['name','price','category','image','description']

class AdminCategories(admin.ModelAdmin):
    list_display=['name','image']

class AdminSpecialItems(admin.ModelAdmin):
    list_display=['Active_InActive_SpecialItem','name','description','image','category','item']


# Register your models here.

admin.site.register(Products,AdminProducts)
admin.site.register(Categories,AdminCategories)
admin.site.register(SpecialItems,AdminSpecialItems)
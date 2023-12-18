from django.contrib import admin
from .models import Category, Handler, Product, WhareHouse

class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProductName', 'Quantity', 'CategoryId', 'WhareHouseId')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('CategoryName', 'CategoryDescription')

class WhareHouseAdmin(admin.ModelAdmin):
    list_display = ('WhareHouseName', 'WhareHouseLocation')

class HandlerAdmin(admin.ModelAdmin):
    list_display = ('HandlerName', 'HandlerSurname', 'HandlerAddress')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WhareHouse, WhareHouseAdmin)
admin.site.register(Handler, HandlerAdmin)
from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount', 'count', 'is_available']
    ...


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Rank)
admin.site.register(models.Tag)
admin.site.register(models.Category)

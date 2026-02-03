from django.contrib import admin

from product.models import Category, Product, Tag

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "created_at", "updated_at")
    list_filter = ("category",)

from django.contrib import admin

from product.models import Category, Product

# Register your models here.

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "created_at", "updated_at")
    list_filter = ("category",)

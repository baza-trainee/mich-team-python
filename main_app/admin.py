from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ProductCategory, Product, ProductImage, SizeQuantity


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class SizeQuantityInline(admin.TabularInline):
    model = SizeQuantity
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_id', 'price')
    inlines = [ProductImageInline, SizeQuantityInline]

admin.site.register(Product, ProductAdmin)

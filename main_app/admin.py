from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ProductCategory, Product, ProductImage, SizeQuantity
from django.utils.html import format_html

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
    list_display = ('id', 'name', 'category_id', 'price', 'display_image')
    list_editable = ('price',)
    inlines = [ProductImageInline, SizeQuantityInline]

    def display_image(self, obj):
        if obj.images.exists():
            return format_html('<img src="{}" width="50" height="50" />', obj.images.first().image.url)
        else:
            return "Немає фото"

    display_image.short_description = 'Фото'

admin.site.register(Product, ProductAdmin)

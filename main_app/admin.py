from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import ProductCategory, Product, ProductImage, SizeQuantity
from django.utils.html import format_html

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    readonly_fields = ('display_images',)
    def display_images(self, obj):
        images_html = ""
        for product_image in obj.product.images.all():
            images_html += format_html('<img src="{}" height="80" />', product_image.image.url)
        return mark_safe(images_html)

    display_images.short_description = 'Фото'


class SizeQuantityInline(admin.TabularInline):
    model = SizeQuantity
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'price', 'display_image', 'is_active',)
    list_editable = ('price', 'is_active',)
    inlines = [ProductImageInline, SizeQuantityInline]
    list_display_links = ('name',)

    def display_image(self, obj):
        if obj.images.exists():
            return format_html('<img src="{}" width="50" height="50" />', obj.images.first().image.url)
        else:
            return "Немає фото"

    display_image.short_description = 'Фото'

admin.site.register(Product, ProductAdmin)

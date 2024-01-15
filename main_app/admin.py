from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProductCategory, Product, ProductImage, SizeQuantity
from django.utils.html import format_html


class ProductCategoryAdmin(admin.ModelAdmin):
    """
        Admin class for managing ProductCategory instances in the Django admin interface.

        This admin class provides a simple list view for ProductCategory instances.
    """
    list_display = ('name',)


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageInline(admin.TabularInline):
    """
        Inline admin for managing ProductImage instances within the Product admin.

        This inline admin displays a tabular view of ProductImage instances associated
        with a Product, including a thumbnail preview of each image.
    """
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
    """
        Inline admin for managing SizeQuantity instances within the Product admin.

        This inline admin displays a tabular view of SizeQuantity instances associated
        with a Product.
    """
    model = SizeQuantity
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    """
        Admin class for managing Product instances in the Django admin interface.

        This admin class provides a list view with additional features such as displaying
        images and managing related instances through inline admins.
    """
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

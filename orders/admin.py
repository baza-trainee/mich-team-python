from django.utils.html import format_html, mark_safe
from django.contrib import admin

from cart.models import Cart
from orders.models import Order


class CartInline(admin.TabularInline):
    """
        Inline admin for Cart model.

        This inline admin is used to display Cart instances within the Order admin.
        It includes a thumbnail view of product images.
    """
    model = Cart
    extra = 0
    exclude = ("session_id", 'is_active')
    readonly_fields = ("product", 'size', 'quantity', "display_images", 'user')

    def display_images(self, obj):
        """
             Display product images as thumbnails.
        """
        images_html = ""
        images_html += format_html('<img src="{}" height="80" />', obj.product.images.first().image.url)
        return mark_safe(images_html)

    display_images.short_description = 'Фото'


class OrderAdmin(admin.ModelAdmin):
    """
        Admin class for Order model.

        This admin class is used to manage Order instances in the Django admin interface.
        It includes a list display, filters, search fields, list editable fields, inlines,
        and read-only fields.
    """
    list_display = ('created_at', 'first_name', 'last_name', 'phone', "delivery_method", "country", 'email',
                    "user", "status")
    list_filter = ('status',)
    search_fields = ('user', 'email', 'user')
    list_editable = ('status',)
    inlines = (CartInline,)
    readonly_fields = ('created_at', 'user')


admin.site.register(Order, OrderAdmin)

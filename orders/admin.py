from django.utils.html import format_html
from django.contrib import admin

from cart.models import Cart
from orders.models import Order

class CartInline(admin.TabularInline):
    model = Cart
    extra = 0
    exclude = ("session_id", 'is_active')
    readonly_fields = ("product", 'size', 'quantity', "display_images", 'user')

    def display_images(self, obj):
        images_html = ""
        for product_image in obj.product.images.all():
            images_html += format_html('<img src="{}" width="50" height="50" />', product_image.image.url)
        return images_html

    display_images.short_description = 'Product Images'



class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'first_name', 'last_name', 'phone', "delivery_method", "country", 'email',
                    "user", "status")
    list_filter = ('status',)
    search_fields = ('user', 'email', 'user')
    list_editable = ('status',)
    inlines = (CartInline,)
    readonly_fields = ('created_at', 'user')



admin.site.register(Order, OrderAdmin)
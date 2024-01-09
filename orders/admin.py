from django.contrib import admin
from django.utils.html import format_html

from cart.models import Cart
from orders.models import Order


class CartInline(admin.TabularInline):
    model = Cart
    extra = 0
    exclude = ("session_id", 'is_active')
    readonly_fields = ("product", 'size', 'quantity', 'user')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'first_name', 'last_name', 'phone', "delivery_method", "country",
                    "street", "city", "state", "zip_code", "user", "status")
    list_filter = ('status',)
    search_fields = ('user',)
    list_editable = ('status',)
    inlines = (CartInline,)
    readonly_fields = ('created_at', 'user')



admin.site.register(Order, OrderAdmin)
from django.contrib import admin
from orders.models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at', 'first_name', 'last_name', 'phone', "delivery_method", "country",
    "street", "city", "state", "zip_code", "user", "status")
    list_filter = ('status',)
    search_fields = ('user',)
    list_editable = ('status',)


admin.site.register(Order, OrderAdmin)
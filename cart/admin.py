from django.contrib import admin

from cart.models import Cart


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Cart, CartAdmin)

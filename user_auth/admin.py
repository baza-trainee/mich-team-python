from django.contrib import admin
from user_auth.models import CustomUser, UserAddresses
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


# Register your models here.
class UserAddressesInline(admin.TabularInline):
    model = UserAddresses
    extra = 1


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_subscribed')
    inlines = [UserAddressesInline]

admin.site.register(CustomUser, CustomUserAdmin)


admin.site.unregister(Group)
admin.site.unregister(BlacklistedToken)
admin.site.unregister(OutstandingToken)

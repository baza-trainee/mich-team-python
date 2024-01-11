from django.contrib import admin
from user_auth.models import CustomUser
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_subscribed')


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(Group)
# admin.site.unregister(Token)
admin.site.unregister(BlacklistedToken)
admin.site.unregister(OutstandingToken)
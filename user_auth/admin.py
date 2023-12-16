from django.contrib import admin
from user_auth.models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_subscribed')



admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin
from .models import EmailSubscribers


class EmailAdmin(admin.ModelAdmin):
    """
        Admin class for managing EmailSubscribers in the Django admin interface.

        This admin class provides a list view with display columns for 'email' and 'is_subscribed'.
    """
    list_display = ['email', 'is_subscribed']


admin.site.register(EmailSubscribers, EmailAdmin)

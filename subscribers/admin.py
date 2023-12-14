from django.contrib import admin
from .models import EmailSubscribers

# Register your models here.
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_subscribed']


admin.site.register(EmailSubscribers, EmailAdmin)
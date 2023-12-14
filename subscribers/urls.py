from django.contrib import admin
from django.urls import path, include

from subscribers.views import email_sender

urlpatterns = [
    path('send_email/', email_sender, name='email_sender'),
]
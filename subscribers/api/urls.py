# subscribers/urls.py
from django.urls import path
from .views import subscribe, unsubscribe

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('unsubscribe/<str:email>/', unsubscribe, name='unsubscribe'),
]

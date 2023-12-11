# In your project's urls.py or an app-specific urls.py
from django.urls import path
from . import views
from .views import UserActivationView, password_reset

urlpatterns = [
    path('user_auth/users/activation/<str:uid>/<str:token>', UserActivationView.as_view(), name='activate_user'),
    path('password/reset/confirm/<str:uid>/<str:token>', password_reset, name='password_reset'),
]

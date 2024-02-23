from django.urls import path, include

from user_auth.api.views import UserAddressView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
    path('', include('djoser.social.urls')),
    path('user_address/', UserAddressView.as_view(), name='user_address_list_create'),
    path('user_address/<int:pk>/', UserAddressView.as_view(), name='user_address_detail'),
]
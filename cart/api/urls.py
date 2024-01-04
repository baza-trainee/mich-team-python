from django.urls import path
from .views import CartItemCreateView

urlpatterns = [
    path('api/cart/', CartItemCreateView.as_view(), name='cart-item-list'),
]

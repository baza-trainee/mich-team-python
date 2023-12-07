from django.urls import path
from .views import OrderListCreateView

urlpatterns = [
    path('api/orders/', OrderListCreateView.as_view(), name='order-list'),
]

from rest_framework import generics, permissions
from .serializers import OrderSerializer
from ..models import Order


class OrderListCreateView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
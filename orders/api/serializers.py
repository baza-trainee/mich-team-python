from rest_framework import serializers

from main_app.api.serializers import ProductOrderSerializer
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    items = ProductOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'delivery_method', 'country',
                  'street',
                  'city', 'state', 'zip_code', 'created_at', 'status', 'user', 'items')

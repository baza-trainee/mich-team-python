from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'delivery_method', 'country', 'street', 'city',
                  'state', 'zip_code', 'created_at')

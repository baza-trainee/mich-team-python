from rest_framework import serializers

from main_app.api.serializers import ProductOrderSerializer
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
        Serializer class for the Order model.

        This serializer is used to convert Order model instances to JSON format
        and vice versa. It includes fields such as id, email, first_name, last_name, etc.
        as well as a nested representation of associated ProductOrder instances under 'items'.
    """
    items = ProductOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'delivery_method', 'country',
                  'street', 'city', 'state', 'zip_code', 'department', 'house_number', 'apartment_number',
                  'created_at', 'status', 'user', 'items')

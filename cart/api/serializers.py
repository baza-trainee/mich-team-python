from rest_framework import serializers
from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    """
        Serializer class for the Cart model.

        This serializer is used to convert Cart model instances to JSON format
        and vice versa.
    """

    class Meta:
        model = Cart
        fields = "__all__"

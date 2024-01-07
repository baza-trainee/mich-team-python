from django.contrib.auth import get_user_model
from rest_framework import serializers
from cart.models import Cart
from main_app.api.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['user', 'session_id', 'product', 'size', 'quantity']

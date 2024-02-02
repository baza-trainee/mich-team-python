from rest_framework import serializers

from cart.models import Cart
from main_app.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'name_en', 'price', 'price_en', 'images']


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

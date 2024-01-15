from rest_framework import serializers
from main_app.models import Product, ProductCategory, ProductImage, SizeQuantity, ProductOrder


class ProductCategorySerializer(serializers.ModelSerializer):
    """
        Serializer class for ProductCategory model.

        This serializer is used to convert ProductCategory model instances to JSON format
        and vice versa.
    """
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    """
        Serializer class for ProductImage model.

        This serializer is used to convert ProductImage model instances to JSON format
        and vice versa.
    """
    class Meta:
        model = ProductImage
        fields = '__all__'


class SizeQuantitySerializer(serializers.ModelSerializer):
    """
        Serializer class for SizeQuantity model.

        This serializer is used to convert SizeQuantity model instances to JSON format
        and vice versa.
    """
    class Meta:
        model = SizeQuantity
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
        Serializer class for Product model.

        This serializer is used to convert Product model instances to JSON format
        and vice versa. It includes nested representations of related models such as
        ProductImage and SizeQuantity.
    """
    images = ProductImageSerializer(many=True, read_only=True)
    sizes_and_quantities = SizeQuantitySerializer(many=True, read_only=True)
    category_name = serializers.ReadOnlyField(source='category_id.name')

    class Meta:
        model = Product
        fields = ['id', 'is_active', 'category_name', 'name', 'name_en', 'price', 'price_en', 'description',
                  'description_en',
                  'composition', 'composition_en', 'category_id', 'images', 'sizes_and_quantities']


class ProductOrderSerializer(serializers.ModelSerializer):
    """
        Serializer class for ProductOrder model.

        This serializer is used to convert ProductOrder model instances to JSON format
        and vice versa.
    """
    class Meta:
        model = ProductOrder
        fields = '__all__'

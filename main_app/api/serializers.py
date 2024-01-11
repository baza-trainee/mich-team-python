from rest_framework import serializers
from main_app.models import Product, ProductCategory, ProductImage, SizeQuantity


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class SizeQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeQuantity
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    sizes_and_quantities = SizeQuantitySerializer(many=True, read_only=True)
    category_name = serializers.ReadOnlyField(source='category_id.name')

    class Meta:
        model = Product
        fields = ['id', 'is_active', 'category_name', 'name', 'name_en', 'price', 'price_en', 'description',
                  'description_en',
                  'composition', 'composition_en', 'category_id', 'images', 'sizes_and_quantities']

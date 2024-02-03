from rest_framework import generics, permissions
from main_app.models import Product, ProductCategory, ProductImage, SizeQuantity
from .serializers import ProductSerializer, ProductCategorySerializer, ProductImageSerializer, SizeQuantitySerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
        Custom token serializer to include the username in the token payload.
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    """
        Custom token view using the custom token serializer.
    """
    serializer_class = MyTokenObtainPairSerializer


class ProductListCreateView(generics.ListAPIView):
    """
        API view for listing and creating products.

        This view provides a list of products and supports creating new products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductDetailView(generics.RetrieveAPIView):
    """
        API view for retrieving a product.

        This view provides detailed information about a specific product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryListView(generics.ListAPIView):
    """
        API view for listing product categories.

        This view provides a list of product categories.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductImageView(generics.ListAPIView):
    """
        API view for listing product images.

        This view provides a list of product images.
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class SizeQuantityView(generics.ListAPIView):
    """
        API view for listing product size and quantity information.

        This view provides a list of size and quantity information related to products.
    """
    queryset = SizeQuantity.objects.all()
    serializer_class = SizeQuantitySerializer

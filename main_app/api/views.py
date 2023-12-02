from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from main_app.models import Product, ProductCategory, ProductImage, SizeQuantity
from .serializers import ProductSerializer, ProductCategorySerializer, ProductImageSerializer, SizeQuantitySerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryListView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductImageView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class SizeQuantityView(generics.ListCreateAPIView):
    queryset = SizeQuantity.objects.all()
    serializer_class = SizeQuantitySerializer

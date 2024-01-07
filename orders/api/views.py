from rest_framework import generics, permissions, status
from rest_framework.response import Response

from cart.models import Cart
from main_app.models import Product
from .serializers import OrderSerializer
from ..models import Order


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    # def post(self, request, *args, **kwargs):
    #     # Получение или создание корзины для пользователя
    #     cart, created = Cart.objects.get_or_create(user=request.user)
    #
    #     # Добавление товаров из корзины в заказ
    #     order_serializer = self.get_serializer(data=request.data)
    #     if order_serializer.is_valid():
    #         order = order_serializer.save(user=request.user)
    #         order.products.set(cart.products.all())  # Перенос товаров из корзины в заказ
    #         cart.products.clear()  # Очистка корзины после оформления заказа
    #
    #         return Response(order_serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class OrderListCreateView(generics.ListCreateAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)
#
#     def perform_create(self, serializer):
#         # Get product ID from the request data
#         product_id = self.request.data.get('product')
#
#         try:
#             # Get the product and related size from the database
#             product = Product.objects.get(id=product_id)
#             size = self.request.data.get('size')  # Assuming you have a 'size' field in your order serializer
#             size_quantity = SizeQuantity.objects.get(product=product, size=size)
#         except Product.DoesNotExist:
#             return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
#         except SizeQuantity.DoesNotExist:
#             return Response({'error': 'Size not found for the selected product'}, status=status.HTTP_404_NOT_FOUND)
#
#         # Perform the order creation
#         serializer.save(user=self.request.user)
#
#         # Decrease the quantity of the product for the selected size
#         size_quantity.quantity -= 1
#         size_quantity.save()
#
#         # Optionally, you can check if the quantity is not negative
#         if size_quantity.quantity < 0:
#             return Response({'error': 'Product is out of stock for the selected size'}, status=status.HTTP_400_BAD_REQUEST)
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
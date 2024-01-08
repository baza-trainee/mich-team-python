from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from cart.models import Cart
from cart.api.serializers import CartSerializer
from django.db.models import Sum
from main_app.models import Product, SizeQuantity


class CartItemCreateView(ListCreateAPIView, DestroyAPIView, UpdateAPIView):
    serializer_class = CartSerializer


    @authentication_classes([])
    @permission_classes([AllowAny])
    def post(self, request, *args, **kwargs):
        request.session.setdefault('init', True)
        request.session.save()
        session_id = request.session.session_key
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)
        size = request.data.get('size')
        user = request.user if request.user.is_authenticated else None

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        if not size and SizeQuantity.objects.filter(product=product).exists():
            return Response({'error': 'Product does not have associated size quantities'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the provided size is valid for the product
        if size and not SizeQuantity.objects.filter(product=product, size=size, quantity__gt=0).exists():
            return Response({'error': "Invalid size for the product"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item = Cart.objects.filter(user=user, session_id=session_id, product=product, size=size).first()


        if cart_item:
            # If the product with the same size already exists, update the quantity
            cart_item.quantity += int(quantity)
            cart_item.save()

            return Response(CartSerializer(cart_item).data, status=status.HTTP_201_CREATED)
        else:
            # If the product does not exist or with a different size, create a new cart item
            cart_item_data = Cart.objects.get_or_create(user=user, session_id=session_id, product=product, size=size,
                                                        quantity=quantity)[0]


            serializer = CartSerializer(cart_item_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request, *args, **kwargs):
        request.session.setdefault('init', True)
        user = request.user if request.user.is_authenticated else None
        session_id = request.session.session_key

        # Получение списка товаров в корзине
        if request.user.is_authenticated:
            Cart.objects.filter(session_id=session_id).update(user=user)
            cart_items = Cart.objects.filter(user=user)
        else:
            cart_items = Cart.objects.filter(session_id=session_id)

        serializer = CartSerializer(cart_items, many=True)

        # Получение общего количества товаров в корзине
        total_items = cart_items.aggregate(total_items=Sum('quantity'))['total_items'] or 0

        response_data = {
            'cart_items': serializer.data,
            'total_items': total_items,
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        size = request.data.get('size')
        user = request.user if request.user.is_authenticated else None
        session_id = request.session.session_key

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_item = Cart.objects.filter(user=user, session_id=session_id, product=product, size=size).first()

        if not cart_item:
            return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

        # Delete the cart item
        cart_item.delete()

        return Response({'message': 'Cart item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



    def update(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        size = request.data.get('size')
        quantity = request.data.get('quantity', 1)
        user = request.user if request.user.is_authenticated else None
        session_id = request.session.session_key


        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_item = Cart.objects.filter(user=user, session_id=session_id, product=product, size=size).first()

        if not cart_item:
            return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the provided size is valid for the product
        if size and not SizeQuantity.objects.filter(product=product, size=size, quantity__gt=0).exists():
            return Response({'error': "Invalid size for the product"}, status=status.HTTP_400_BAD_REQUEST)

        # Update the quantity
        cart_item.quantity = int(quantity)
        cart_item.save()

        serializer = CartSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)


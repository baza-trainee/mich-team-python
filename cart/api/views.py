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
    """
        API view for handling operations related to the shopping cart.

        This view allows creating, updating, listing, and deleting cart items.
        It also provides information about the current contents of the shopping cart.

        Supported HTTP Methods:
            - POST: Create a new cart item or update an existing one.
            - GET: Retrieve the current contents of the shopping cart.
            - DELETE: Remove a product from the shopping cart.
            - PUT/PATCH: Update the quantity and size of a product in the shopping cart.

        Fields:
            - product: The ID of the product.
            - quantity: The quantity of the product.
            - size: The size of the product.
            - new_size: The new size to update the product in the cart.

        Example:
        ```
        POST /cart/
        {
            "product": 1,
            "quantity": 2,
            "size": "M"
        }

        GET /cart/

        DELETE /cart/
        {
            "product": 1,
            "size": "M"
        }

        PUT /cart/
        {
            "product": 1,
            "quantity": 3,
            "size": "M",
            "new_size": "L"
        }
        ```
    """

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

        if size and not SizeQuantity.objects.filter(product=product, size=size, quantity__gt=0).exists():
            return Response({'error': "Invalid size for the product"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item = Cart.objects.filter(user=user, session_id=session_id, product=product, size=size,
                                        is_active=True).first()

        if cart_item:
            cart_item.quantity += int(quantity)
            cart_item.save()

            return Response(CartSerializer(cart_item).data, status=status.HTTP_201_CREATED)
        else:
            cart_item_data = Cart.objects.get_or_create(user=user, session_id=session_id, product=product, size=size,
                                                        quantity=quantity, is_active=True)[0]

            serializer = CartSerializer(cart_item_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        request.session.setdefault('init', True)
        user = request.user if request.user.is_authenticated else None
        session_id = request.session.session_key

        if request.user.is_authenticated:
            Cart.objects.filter(session_id=session_id).update(user=user)
            cart_items = Cart.objects.filter(user=user, is_active=True)
        else:
            cart_items = Cart.objects.filter(session_id=session_id, is_active=True)

        serializer = CartSerializer(cart_items, many=True)

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

        cart_item = Cart.objects.filter(user=user, session_id=session_id, product=product, size=size,
                                        is_active=True).first()

        if not cart_item:
            return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()

        return Response({'message': 'Cart item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        size = request.data.get('size')
        quantity = request.data.get('quantity', 1)
        user = request.user if request.user.is_authenticated else None
        session_id = request.session.session_key
        new_size = request.data.get('new_size')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_item = Cart.objects.filter(user=user, session_id=session_id, product=product, size=size,
                                        is_active=True).first()

        if not cart_item:
            return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

        if size and not SizeQuantity.objects.filter(product=product, size=size, quantity__gt=0).exists():
            return Response({'error': "Invalid size for the product"}, status=status.HTTP_400_BAD_REQUEST)

        if new_size and not SizeQuantity.objects.filter(product=product, size=new_size, quantity__gt=0).exists():
            return Response({'error': "Invalid new_size for the product"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item.quantity = int(quantity)
        cart_item.size = new_size
        cart_item.save()

        serializer = CartSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from cart.models import Cart
from cart.api.serializers import CartSerializer
from django.db.models import Sum
from main_app.models import Product

class CartItemCreateView(ListCreateAPIView):
    serializer_class = CartSerializer

    @authentication_classes([])
    @permission_classes([AllowAny])
    def post(self, request, *args, **kwargs):
        request.session.setdefault('init', True)
        request.session.save()
        session_id = request.session.session_key
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)
        user = request.user if request.user.is_authenticated else None

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_item = Cart.objects.filter(user=user, session_id=session_id, product=product).first()
        print(cart_item)

        if cart_item:
            # If the product already exists, update the quantity
            cart_item.quantity += int(quantity)
            cart_item.save()
            return Response({'success': 'Product quantity updated'}, status=status.HTTP_201_CREATED)
        else:
            # If the product does not exist, create a new cart item
            cart_item_data = {
                'user': user.pk if user else None,
                'session_id': session_id,
                'product': product.pk,
                'quantity': quantity,
            }

            serializer = CartSerializer(data=cart_item_data)
            print(cart_item_data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer.is_valid(raise_exception=True)  # Ensure is_valid() is called before accessing errors

        if serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)

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
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from cart.models import Cart
from main_app.models import ProductOrder
from .serializers import OrderSerializer
from ..models import Order

CustomUser = get_user_model()

class OrderListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating orders.

    Attributes:
        serializer_class: The serializer class for orders.
        permission_classes: A list of permission classes allowing any user to access this view.
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Get the queryset of orders based on the user's authentication status.

        Returns:
            QuerySet: A filtered queryset based on the user's authentication status.
        """
        user = self.request.user if self.request.user.is_authenticated else None

        return Order.objects.filter(user=user)

    def get_session_id(self, request):
        """
        Get the session ID from the request.

        Args:
            request: The request object.

        Returns:
            str: The session ID.
        """
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key
        return session_key

    def process_carts(self, carts, order):
        """
        Process the carts associated with an order.

        Args:
            carts (QuerySet): The carts to be processed.
            order (Order): The order to associate carts with.

        Returns:
            Response: A response indicating success or failure.
        """
        for cart in carts:
            cart_product = cart.product
            ProductOrder.objects.create(category_id=cart_product.category_id,
                                        category_name=cart_product.category_id.name,
                                        name=cart_product.name,
                                        name_en=cart_product.name_en,
                                        price=cart_product.price,
                                        price_en=cart_product.price_en,
                                        description=cart_product.description,
                                        description_en=cart_product.description_en,
                                        composition=cart_product.composition,
                                        composition_en=cart_product.composition_en,
                                        size=cart.size,
                                        quantity=cart.quantity,
                                        order=order)

            size_quantity_found = False  # Flag to check if a matching size is found

            for size_quantity in cart_product.sizes_and_quantities.all():
                if size_quantity.size == cart.size and size_quantity.quantity >= cart.quantity:
                    size_quantity.quantity -= cart.quantity
                    size_quantity.save()
                    cart.is_active = False
                    cart.save()
                    size_quantity_found = True
                    break  # Exit the loop once a match is found

            # Check if a matching size was not found
            if not size_quantity_found:
                order.delete()
                return Response({'error': 'Ordered quantity exceeds available stock for product "{}"'.format(
                    cart_product.name)}, status=status.HTTP_400_BAD_REQUEST)

        return None

    def post(self, request, *args, **kwargs):
        """
        Handle the creation of a new order.

        Args:
            request: The request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response indicating success or failure.
        """
        phone = request.data.get("phone")
        delivery_method = request.data.get("delivery_method")
        country = request.data.get("country")
        street = request.data.get("street")
        city = request.data.get("city")
        state = request.data.get("state")
        zip_code = request.data.get("zip_code")
        product_data = request.data.get("product")

        session_id = request.session.session_key

        user = request.user if request.user.is_authenticated else None
        user_id = user.id if user and user.is_authenticated else None
        email = user.email if user and user.is_authenticated else request.data.get("email")
        first_name = user.first_name if user and user.is_authenticated else request.data.get("first_name")
        last_name = user.last_name if user and user.is_authenticated else request.data.get("last_name")

        response_data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "delivery_method": delivery_method,
            "country": country,
            "street": street,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            'user': user_id,
            'product': product_data
        }

        order_serializer = OrderSerializer(data=response_data)

        if order_serializer.is_valid():

            order = order_serializer.save(user=user)

            # Handle associating carts with the order
            if user and user.is_authenticated:
                user_carts = Cart.objects.filter(user=user, is_active=True)
                user_carts.update(order=order)

                response = self.process_carts(user_carts, order)
                if response:
                    return response
            else:
                session_carts = Cart.objects.filter(session_id=session_id, is_active=True)
                session_carts.update(order=order)

                response = self.process_carts(session_carts, order)
                if response:
                    return response

            return Response(order_serializer.data, status=status.HTTP_201_CREATED)

        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """
        Handle the retrieval of orders.

        Args:
            request: The request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response containing the list of orders or an error message.
        """
        queryset = self.get_queryset()
        if request.user and request.user.is_authenticated:
            return Response(self.get_serializer(queryset, many=True).data)

        return Response({"error": "User is unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView

from .serializers import CustomUserSerializer, UserAddressSerializer
from ..models import CustomUser
from user_auth.models import UserAddresses
from rest_framework.response import Response
from rest_framework import status


class CustomUserView(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(email=self.request.user)

    def get_object(self):
        return self.get_queryset().first()

    def update(self, request, *args, **kwargs):
        request.data.pop('password', None)

        return super().update(request, *args, **kwargs)


class UserAddressView(ListCreateAPIView, DestroyAPIView, UpdateAPIView):
    serializer_class = UserAddressSerializer

    def get_queryset(self):
        return UserAddresses.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        delivery_method = request.data.get('delivery_method')
        country = request.data.get('country')
        street = request.data.get('street')
        city = request.data.get('city')
        state = request.data.get('state')
        zip_code = request.data.get('zip_code')
        department = request.data.get('department')
        house_number = request.data.get('house_number')
        apartment_number = request.data.get('apartment_number')

        # Check if the user is authenticated
        if not user:
            return Response({'error': "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        # Check if an address already exists
        address_data = UserAddresses.objects.filter(
            user=user,
            delivery_method=delivery_method,
            country=country,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            department=department,
            house_number=house_number,
            apartment_number=apartment_number
        ).first()

        if address_data:
            return Response({'error': "Address already in database"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Address does not exist, create a new record
            new_address_data = UserAddresses(
                user=user,
                delivery_method=delivery_method,
                country=country,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code,
                department=department,
                house_number=house_number,
                apartment_number=apartment_number
            )
            new_address_data.save()

            # Return the newly created address
            serializer = UserAddressSerializer(new_address_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        if not user:
            return Response({'error': "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        addresses = UserAddresses.objects.filter(user=user)
        serializer = UserAddressSerializer(addresses, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        if not user:
            return Response({'error': "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        if not user:
            return Response({'error': "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

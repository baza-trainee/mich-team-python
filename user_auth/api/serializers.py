from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from ..models import CustomUser, UserAddresses


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'is_subscribed', 'password', 'phone')

    password = serializers.CharField(write_only=True, required=False)

    def validate(self, data):
        if 'password' in data and data['password'] == '':
            del data['password']

        return data

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        password = validated_data.get('password')

        if password:
            instance.set_password(password)

        return super().update(instance, validated_data)

class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddresses
        fields = ['id', 'delivery_method', 'country', 'street', 'city', 'state', 'zip_code', 'department',
                  'house_number',
                  'apartment_number']




from rest_framework import serializers
from subscribers.models import EmailSubscribers


class SubscriberSerializer(serializers.ModelSerializer):
    """
        Serializer class for EmailSubscribers model.

        This serializer is used to convert EmailSubscribers model instances to JSON format
        and vice versa. It includes fields such as 'email' and 'is_subscribed'.
    """

    class Meta:
        model = EmailSubscribers
        fields = ['email', 'is_subscribed']

from rest_framework import serializers
from subscribers.models import EmailSubscribers

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscribers
        fields = ['email', 'is_subscribed']
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from subscribers.models import EmailSubscribers
from .serializers import SubscriberSerializer


class SubscribeView(generics.CreateAPIView):
    """
    API view for subscribing to email notifications.

    This view allows users to subscribe to email notifications by providing
    their email address. If the email address is valid, it is added to the
    list of subscribers.

    Serializer Class:
        SubscriberSerializer: Serializer for handling subscription data.

    HTTP Methods:
        - POST: Creates a new subscription.

    Response status codes:
        - 201 Created: Subscription created successfully.
        - 400 Bad Request: Invalid data provided.

    Example:
    ```
    POST /subscribe/
    {
        "email": "example@example.com",
        "is_subscribed": true
    }
    ```

    """
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        """
            Handle POST requests for creating a new subscription.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnsubscribeView(generics.DestroyAPIView):
    """
        API view for unsubscribing from email notifications.

        This view allows users to unsubscribe from email notifications by providing
        their email address. If the email address is found in the list of subscribers,
        it is removed.

        Serializer Class:
            SubscriberSerializer: Serializer for handling subscription data.

        HTTP Methods:
            - DELETE: Removes a subscription.

        Response status codes:
            - 204 No Content: Unsubscription successful.
            - 404 Not Found: Email address not found in the list of subscribers.

        Example:
        ```
        DELETE /unsubscribe/example@example.com/
        ```

    """
    queryset = EmailSubscribers.objects.all()
    lookup_field = 'email'
    serializer_class = SubscriberSerializer

    def destroy(self, request, *args, **kwargs):
        """
            Handle DELETE requests for removing a subscription.
        """
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except EmailSubscribers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

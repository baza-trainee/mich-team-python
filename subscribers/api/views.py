from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from subscribers.models import EmailSubscribers
from .serializers import SubscriberSerializer

class SubscribeView(generics.CreateAPIView):
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnsubscribeView(generics.DestroyAPIView):
    queryset = EmailSubscribers.objects.all()
    lookup_field = 'email'
    serializer_class = SubscriberSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except EmailSubscribers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
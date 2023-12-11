# subscribers/views.py
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from subscribers.models import EmailSubscribers
from .serializers import SubscriberSerializer

@api_view(['POST'])
def subscribe(request):
    serializer = SubscriberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def unsubscribe(request, email):
    try:
        subscriber = EmailSubscribers.objects.get(email=email)
        subscriber.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except EmailSubscribers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

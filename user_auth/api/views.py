from rest_framework import generics
from .serializers import CustomUserSerializer
from ..models import CustomUser

class CustomUserView(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(email=self.request.user)

    def get_object(self):
        return self.get_queryset().first()

    def update(self, request, *args, **kwargs):
        request.data.pop('password', None)

        return super().update(request, *args, **kwargs)

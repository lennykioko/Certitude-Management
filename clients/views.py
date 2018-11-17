from rest_framework import generics, permissions

from . import models
from . import serializers


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            if request.method in ['PUT', 'DELETE']:
                return False


class ListCreateClient(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class RetrieveUpdateDestroyClient(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUser,)
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

from .models import *
from .serializers import *
from rest_framework import viewsets, permissions


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserDataSerializer

class SessionDataViewSet(viewsets.ModelViewSet):
    queryset = SessionData.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SessionDataSerializer

class SessionListViewSet(viewsets.ModelViewSet):
    queryset = SessionList.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SessionListSerializer
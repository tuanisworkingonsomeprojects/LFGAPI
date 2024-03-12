from rest_framework import serializers
from .models import *

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class SessionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionData
        fields = '__all__'


class SessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionList
        fields = '__all__'



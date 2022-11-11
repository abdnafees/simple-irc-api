'''
This file contains Serializer class for the Customauth model.
'''
from rest_framework import serializers

from customauth.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields: str = '__all__'


class CustomUserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields: list[str] = ['username', 'password', 'email']

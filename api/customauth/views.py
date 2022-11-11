'''
A view function, or view for short, is a Python function that takes a web request and returns a web response. 
'''

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from customauth.models import CustomUser
from customauth.serializers import (
    CustomUserLoginSerializer, CustomUserSerializer,
)


class ListUsers(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RegisterUser(CreateAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = CustomUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['username']
        token, created = Token.objects.get(user=user.pk)

        return Response(
            {'token': token.key, 'username': user.username, 'email': user.email},
            status=status.HTTP_200_OK,
        )

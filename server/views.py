from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Server
from .serializers import ServerSerializer


class ServerList(ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class CreateServer(CreateAPIView):
    serializer_class = ServerSerializer

    def post(self, request):
        serializer = ServerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

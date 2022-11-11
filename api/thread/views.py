'''
A view function, or view for short, is a Python function that takes a web request and returns a web response. 
'''
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from .models import Thread
from .serializers import ChatMessageSerializer, ThreadSerializer


class ThreadCreateView(CreateAPIView):
    serializer_class = ThreadSerializer

    def post(self, request):
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThreadListView(ListAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class SendMessageView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChatMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

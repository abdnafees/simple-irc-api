from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Server
from .serializers import ServerSerializer


class ServerList(ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class CreateServer(CreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

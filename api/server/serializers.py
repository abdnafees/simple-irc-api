'''
This file contains Serializer class for the Server model.
'''
from rest_framework import serializers

from server.models import Server


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = "__all__"

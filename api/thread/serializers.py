from rest_framework import serializers

from .models import ChatMessage, Thread


class ChatMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMessage
        fields = "__all__"


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = "__all__"

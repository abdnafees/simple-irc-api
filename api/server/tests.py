'''
This file for tests for the Server API endpoint.
'''
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Server


class ServerTests(APITestCase):

    def test_create_server(self):

        url = reverse("create-server")
        data = {
            "network_name": "test_network1",
            "hostname": "127.0.0.1",
            "port": "8001",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Server.objects.count(), 1)
        self.assertEqual(Server.objects.get().network_name, "test_network1")

'''
This files contains tests for the Thread API endpoint.
'''

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Thread


class ThreadTests(APITestCase):

    def test_create_thread(self):
        url = reverse("create-thread")
        data = {
            "server": "test_network1",
            "name": "#hello",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Thread.objects.count(), 1)
        self.assertEqual(Thread.objects.get().network_name, "test_network1")

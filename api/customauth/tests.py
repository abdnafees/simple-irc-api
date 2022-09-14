from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CustomUser


class CustomAuthTests(APITestCase):
    def test_create_user(self):
        url = reverse("create-user")
        data = {
            "username": "testuser1",
            "server": "1",
            "email": "test1@gmail.com",
            "password": "123456",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, "testuser1")

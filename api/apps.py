'''
Configuration file for group IRC application and API.

This file exposes AppConfig class to INSTALLED_APPS.
'''
from django.apps import AppConfig


class ApiConfig(AppConfig):

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

'''
Configuration file for Server application.

This file exposes AppConfig class to INSTALLED_APPS.
'''

from django.apps import AppConfig


class ServerConfig(AppConfig):
    '''Extends AppConfig class for application configuration'''

    default_auto_field = "django.db.models.BigAutoField"
    name = "server"

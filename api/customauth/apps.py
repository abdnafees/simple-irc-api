'''
Configuration file for Customauth application.

This file exposes AppConfig class to INSTALLED_APPS.
'''
from django.apps import AppConfig


class CustomauthConfig(AppConfig):
    '''Extends AppConfig class for application configuration'''

    default_auto_field: str = 'django.db.models.BigAutoField'
    name = 'customauth'

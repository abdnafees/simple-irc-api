'''
SECURITY WARNING: don't run with debug turned on in production!
'''
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]

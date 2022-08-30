from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import CustomUserManager
from server.models import Server


class CustomUser(AbstractBaseUser):
    username = models.CharField(verbose_name="username", max_length=255, unique=True)
    email = models.EmailField(verbose_name="email_address", max_length=255)
    password = models.CharField(verbose_name="password", max_length=10)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    objects = CustomUserManager()
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self) -> str:
        return self.nickname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

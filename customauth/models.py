from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from server.models import Server


class CustomUserManager(BaseUserManager):
    def create_user(self, validated_data):

        if not validated_data["username"]:
            raise ValueError("User must have a unique username.")

        user = self.model(
            email=self.normalize_email(validated_data["email"]),
            username=validated_data["username"],
            server=validated_data["server"],
        )

        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(verbose_name="username", max_length=255, unique=True)
    email = models.EmailField(verbose_name="email_address", max_length=255)
    password = models.CharField(verbose_name="password", max_length=1024)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    objects = CustomUserManager()
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

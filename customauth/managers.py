from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, validated_data):
        if not validated_data["email"]:
            raise ValueError("User must have a unique username.")

        user = self.model(
            email=self.normalize_email(validated_data["email"]),
            username=validated_data["username"],
        )

        user.set_password(validated_data["password"])
        user.save(using=self._db)
        return user

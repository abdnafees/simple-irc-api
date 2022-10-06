# Generated by Django 4.1 on 2022-09-07 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("server", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="username"
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=255, verbose_name="email_address"),
                ),
                ("password", models.CharField(max_length=10, verbose_name="password")),
                (
                    "server",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="server.server"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
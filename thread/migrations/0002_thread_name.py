# Generated by Django 4.1 on 2022-09-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thread", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="thread",
            name="name",
            field=models.CharField(default=None, max_length=255),
        ),
    ]

# Generated by Django 4.1 on 2022-09-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customauth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(max_length=1024, verbose_name="password"),
        ),
    ]
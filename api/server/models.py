from django.db import models


class Server(models.Model):
    network_name = models.CharField(max_length=255)
    hostname = models.CharField(max_length=63)
    port = models.IntegerField(default=6667)

    def __str__(self):
        return self.network_name

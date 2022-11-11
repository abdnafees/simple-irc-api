''''
A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data youre storing. 
Generally, each model maps to a single database table.

The basics:

Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API; see Making queries.
'''
from django.db import models

from api.customauth.models import CustomUser
from api.server.models import Server


class Thread(models.Model):

    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.messages


class ChatMessage(models.Model):

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message

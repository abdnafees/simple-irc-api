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


class Server(models.Model):

    network_name = models.CharField(max_length=255)
    hostname = models.CharField(max_length=63)
    port = models.IntegerField(default=6667)

    def __str__(self):
        return self.network_name

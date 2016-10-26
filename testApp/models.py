from __future__ import unicode_literals

from django.db import models


class Test(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username

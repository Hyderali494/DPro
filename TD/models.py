from __future__ import unicode_literals

from django.db import models

class Register(models.Model):
    username = models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    Email    = models.CharField(max_length = 150)
    Phone_no = models.IntegerField(default = 0)

# Create your models here.

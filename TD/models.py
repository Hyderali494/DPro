from __future__ import unicode_literals

from django.db import models

class Register(models.Model):
    username = models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    Email    = models.CharField(max_length = 150)
    Phone_no = models.IntegerField(default = 0)
    def __str__(self):
        return self.username;

class Contact(models.Model):
    Username = models.CharField(max_length = 50)
    Nickname = models.CharField(max_length = 50)
    Phone_no = models.BigIntegerField(default = 0)
    Email = models.CharField(max_length = 50)
    Company = models.CharField(max_length = 50)
    def __str__(self):
        return self.Username;

# Create your models here.

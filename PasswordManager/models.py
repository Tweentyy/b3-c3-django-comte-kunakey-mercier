from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=1000)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

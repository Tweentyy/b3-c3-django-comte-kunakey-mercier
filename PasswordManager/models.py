from django.db import models
import uuid

class Site(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=1000)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Connect(models.Model):

    api_key = models.CharField(max_length=200)
    secret_key = models.CharField(max_length=200)

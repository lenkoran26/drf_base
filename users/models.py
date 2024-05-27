from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

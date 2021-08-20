from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractUser):
    naegong = models.IntegerField(default=0, null=True)
    manner = models.IntegerField(default=0, null=True)
    def __str__(self):
        return self.username
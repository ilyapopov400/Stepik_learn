from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username


class Notes(models.Model):
    note = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

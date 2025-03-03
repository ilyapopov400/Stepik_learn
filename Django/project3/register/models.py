from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    def create_user(self, username, first_name, last_name, email, password1):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password1)
        self.save()

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    def __str__(self):
        return self.username




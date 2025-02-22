from django.db import models
from register import models as register_models


# Create your models here.

class Notes(models.Model):
    note = models.TextField()
    user = models.ForeignKey(register_models.CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

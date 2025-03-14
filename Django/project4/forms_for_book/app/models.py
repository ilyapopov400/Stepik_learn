from django.db import models


# Create your models here.

class Books(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=10)

    def __str__(self):
        if len(self.title) < 7:
            text = "{} - {}".format(self.author, self.title)
        else:
            text = "{} - {}".format(self.author, self.title[:7])
        return text

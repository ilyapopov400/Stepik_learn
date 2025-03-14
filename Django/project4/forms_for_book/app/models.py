from django.db import models


# Create your models here.

class Books(models.Model):
    author = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        if len(self.content) < 7:
            text = "{} - {}".format(self.author, self.content)
        else:
            text = "{} - {}".format(self.author, self.content[:7])
        return text

from django.db import models

# Create your models here.

class data(models.Model):
    penulis = models.CharField(max_length=255)
    awalberdiri = models.TextField()

    def __str__(self):
        return "{}".format(self.penulis)
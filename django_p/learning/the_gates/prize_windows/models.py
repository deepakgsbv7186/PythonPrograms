from django.db import models

# Create your models here.

class contacting(models.Model):
    email = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    date =  models.DateField()

    def __str__(self):
        return self.email
from django.db import models

# Create your models here.

class uploadimg(models.Model):
    name = models.CharField(max_length=30)
    catagory = models.CharField(max_length=50 , default='unknown')
    pic = models.ImageField(upload_to='wallpaper' )

    def __str__(self):
        return self.name



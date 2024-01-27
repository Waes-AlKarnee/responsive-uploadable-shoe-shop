from django.db import models

# Create your models here.

class shoe(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    Img = models.ImageField(upload_to='UserShoeImage')
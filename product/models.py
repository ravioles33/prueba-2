from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,)
    type = models.CharField(max_length=255,)
    price = models.IntegerField()
    in_promotion = models.BooleanField()
    highlighted = models.BooleanField()
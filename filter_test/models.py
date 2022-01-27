from django.db import models

class Product(models.Model):
    P_Name = models.CharField(max_length=15)
    Price = models.IntegerField( default = True)
    Ratings = models.IntegerField()
    Number = models.IntegerField()
    date = models.DateField()

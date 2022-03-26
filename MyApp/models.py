from pyexpat import model
from django.db import models

# Create your models here.

class Customer(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    no_hp =  models.CharField(max_length=12)


    def __str__(self):
        return self.fullname
    
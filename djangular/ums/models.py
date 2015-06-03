from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    mobile = models.CharField(max_length=50)
    dob = models.DateTimeField('date published')

from urllib import request
from django.db import models

# Create your models here.
class login(models.Model):
    fist_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
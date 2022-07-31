from django.db import models
from matplotlib import image


 
# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)

class Detail(models.Model):
    username=models.CharField(max_length=20)
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    mobno=models.CharField(max_length=10)
    role =models.CharField(max_length=10)
    weight=models.IntegerField()
    height=models.IntegerField()
    address=models.CharField(max_length=30)
    addtype=models.CharField(max_length=10)
    idtype=models.CharField(max_length=10)
    idno=models.IntegerField()
    job=models.CharField(max_length=20)
    image=models.ImageField(upload_to='pictures')

    
    

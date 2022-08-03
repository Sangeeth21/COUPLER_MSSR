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
    
class Detaila(models.Model):
    username=models.CharField(max_length=20)
    describeu=models.CharField(max_length=50)
    age=models.IntegerField()
    qualification=models.CharField(max_length=20)
    education=models.CharField(max_length=20)
    professionalexp=models.CharField(max_length=20)
    mothertongue=models.CharField(max_length=20)
    describeurfamily=models.CharField(max_length=100)
    familytype=models.CharField(max_length=100)
    familyvalue=models.CharField(max_length=100)
    familystatus=models.CharField(max_length=100)
    maritalstatus=models.CharField(max_length=100)
    hobbiesandinterest=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=10)
    city=models.CharField(max_length=10)

class Preference1(models.Model):
    username=models.CharField(max_length=20)
    personallyf=models.CharField(max_length=20)
    adoptchild=models.CharField(max_length=20)
    lifewithdiv=models.CharField(max_length=20)
    ambitious=models.CharField(max_length=20)
    superstitious=models.CharField(max_length=20)
    

class Preference2(models.Model):
    username=models.CharField(max_length=20)
    socialcom=models.CharField(max_length=20)
    partnertalent=models.CharField(max_length=20)
    partnerindep=models.CharField(max_length=20)
    drinkorsmoke=models.CharField(max_length=20)
    hangout=models.CharField(max_length=20)



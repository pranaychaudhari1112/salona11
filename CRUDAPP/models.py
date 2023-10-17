from django.db import models

# Create your models here.

class saloona(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    massege = models.TextField()
    phone = models.IntegerField()

def  __str__(self):
    return self.name


class business(models.Model):
    yourbusiness = models.CharField(max_length=300)
    yourname = models.CharField(max_length=300)
    mobilenumber = models.IntegerField()
    emailaddress = models.EmailField()
    business=models.CharField(max_length=200)
def  __str__(self):
    return self.name


from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    Gstin=models.CharField(max_length=15,unique=True)
    Address1=models.CharField(max_length=1000)
    Address2=models.CharField(max_length=1000)
    Trade_name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pincode=models.IntegerField(null=True)
class Customer(models.Model):
    fromGstin=models.CharField(max_length=15,unique=True)
    fromTrdName=models.CharField(max_length=50)
    fromAddr1=models.CharField(max_length=1000)
    fromplace=models.CharField(max_length=100)
    frompincode=models.IntegerField(null=True)
    toGstin=models.CharField(max_length=15,unique=True)
    toTrdName=models.CharField(max_length=50)
    toAddr1=models.CharField(max_length=1000)
    toplace=models.CharField(max_length=100)
    topincode=models.IntegerField(null=True)
    otherValue=models.IntegerField(null=True)
    vehicleNo=models.CharField(max_length=20)
    vehicleType=models.CharField(max_length=20)

class Item(models.Model):
    productName=models.CharField(max_length=20)
    productDesc=models.CharField(max_length=20)
    quantity=models.IntegerField(null=True)
    qtyUnit=models.CharField(max_length=20)
    taxableAmount=models.IntegerField(null=True)


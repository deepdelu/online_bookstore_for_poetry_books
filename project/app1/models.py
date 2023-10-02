from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6,default="")
    email=models.CharField(max_length=20,default="")
    address=models.CharField(max_length=100,default="")
    class Meta:
        db_table="registration"
class cont(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    message=models.CharField(max_length=100)
    class Meta:
        db_table="cont"        
class base(models.Model):
    email=models.CharField(max_length=20,default="")
    class Meta:
        db_table="base"
class prod(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    pic=models.ImageField(upload_to='prod/')
    description=models.CharField(max_length=10000, default="Description")
    class Meta:
        db_table="prod"
    def __str__(self):
        return self.name

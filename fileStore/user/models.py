from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Profile(AbstractUser):
     remainMoney=models.SmallIntegerField(default=0,blank=True,null=True)
     class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Profile' 

class Admin(models.Model):
     user=models.OneToOneField(to="Profile",on_delete=models.CASCADE)

class Customer(models.Model):
     user=models.OneToOneField(to="Profile",on_delete=models.CASCADE)
     store=models.ManyToManyField(to="store.Store",null=True,blank=True,through="StoreCustomer")
     product=models.ManyToManyField(to="production.Product",null=True,blank=True)
     _file=models.ManyToManyField(to="production.File",null=True,blank=True)

class StoreCustomer(models.Model):
     customer=models.ForeignKey(to="Customer",on_delete=models.CASCADE)
     store=models.ForeignKey(to="store.Store",on_delete=models.CASCADE)
     expire_time=models.DateField()
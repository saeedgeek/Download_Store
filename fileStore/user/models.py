from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Profile(AbstractUser):
     remainMoney=models.SmallIntegerField()
     class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Profile' 

class Admin(models.Model):
     user=models.OneToOneField(Profile,on_delete=models.CASCADE)

class Customer(models.Model):
     user=models.OneToOneField(Profile,on_delete=models.CASCADE)


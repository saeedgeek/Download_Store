from django.db import models
# Create your models here.
class Store(models.Model):
     membershipPrice=models.SmallIntegerField()
     admin=models.ForeignKey(to="user.Admin",on_delete=models.CASCADE)
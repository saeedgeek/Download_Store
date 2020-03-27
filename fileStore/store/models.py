from django.db import models
# Create your models here.
class Store(models.Model):
     name=models.CharField(max_length=20,primary_key=True)
     price=models.SmallIntegerField()
     admin=models.ForeignKey(to="user.Admin",on_delete=models.CASCADE,related_name="admin")
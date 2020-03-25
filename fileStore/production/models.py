from django.db import models
# Create your models here.
class Product(models.Model):
     name=models.CharField(max_length=20)
     fee=models.SmallIntegerField()
     store=models.ForeignKey(to="store.Store",on_delete=models.CASCADE)
     category=models.ForeignKey(to="Category",on_delete=models.CASCADE)

class File(models.Model):
     name=models.CharField(max_length=20)
     product=models.ForeignKey(to="Product",on_delete=models.CASCADE)

class Category(models.Model):
     name=models.CharField(max_length=20,primary_key=True)


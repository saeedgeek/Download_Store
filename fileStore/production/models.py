from django.db import models
# Create your models here.
class Product(models.Model):
     name=models.CharField(max_length=20)
     fee=models.SmallIntegerField()
     store=models.ForeignKey(to="store.Store",on_delete=models.CASCADE,related_name="product")
     category=models.ForeignKey(to="Category",on_delete=models.CASCADE,related_name="product")

class File(models.Model):
     name=models.CharField(max_length=20)
     content=models.FileField(upload_to='files')
     caption=models.CharField(max_length=200)
     product=models.ForeignKey(to="Product",on_delete=models.CASCADE,related_name="file")

class Category(models.Model):
     name=models.CharField(max_length=20,primary_key=True)

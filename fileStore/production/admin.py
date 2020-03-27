from django.contrib import admin
from .models import Category,File,Product
# Register your models here.
admin.site.register(Category)
admin.site.register(File)
admin.site.register(Product)
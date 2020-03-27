from .models import Category,Product,File
from rest_framework import serializers

class CategourySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["name"]
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["name"]

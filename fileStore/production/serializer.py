from .models import Category,Product,File
from rest_framework import serializers

class CategourySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["name"]
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"


""" this and """
class ProductShowListSerializer(serializers.ModelSerializer):
    """it is for showing data"""
    class Meta:
        model=Product
        fields=["id","name","fee","category","store"]


class ProductGetListSerializer(serializers.ModelSerializer):
    """ it is for getting data """
    class Meta:
        model=Product
        fields=["store"]




""" this and """
class FileShowListSerializer(serializers.ModelSerializer):
    """it is for showing data"""
    class Meta:
        model=File
        fields=["id","name","caption","product","fee"]

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        fields="__all__"


class FileGetListSerializer(serializers.ModelSerializer):
    """ it is for getting data """
    class Meta:
        model=File
        fields=["product"]

class BuyDownloadFileProducterializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    class Meta:
        model=File
        fields=["id"]


class BuyDownloadFileSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=True)
    class Meta:
        model=File
        fields = ["id"]

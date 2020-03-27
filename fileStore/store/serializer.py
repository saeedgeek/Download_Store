from rest_framework import serializers
from .models import Store
from user.models import  Admin
class StoreSerializer(serializers.ModelSerializer):
     class Meta:
          model=Store
          fields=["name","price"]
     def create(self,validate_data):
          request = self.context.get("request")
          profile = request.user
          admin=Admin.objects.get(user=profile)
          store=Store.objects.create(
               name=validate_data["name"],
               price=validate_data["price"],
               admin=admin
               
               )
          return store

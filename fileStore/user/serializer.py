from rest_framework import serializers
from .models import Profile,Admin,Customer

class RegisterSerializer(serializers.ModelSerializer):
     user_type = serializers.CharField()
     class Meta:
          model=Profile
          fields=['username','password','email','user_type']
     def create(self, validated_data):
          print("..................................in the serializer")
          profile = Profile.objects.create_user(
               username=validated_data["username"] ,
               password=validated_data["password"] ,
               email=validated_data["email"] ,
               )
          
          if validated_data["user_type"].startswith("A") or validated_data["user_type"].startswith("a"):
               Admin.objects.create(user=profile)
          else:
               Customer.objects.create(user=profile)     
          return profile

class ChargingSerializer(serializers.ModelSerializer):
     credit=serializers.IntegerField(required=True)
     class Meta:
          model=Profile
          fields=['credit',]


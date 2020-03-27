from django.shortcuts import render
from rest_framework.views import APIView
from  .serializer import RegisterSerializer
from utils.Response import response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import Profile

# Create your views here.


class Register(APIView):
     serializer_class=RegisterSerializer
     def post(self,request):
          serializer=self.serializer_class(data=request.data)
          if(serializer.is_valid()):
               serializer.save()
               msg="user "+request.data["username"]+" registerd successFully"
               return  response(condition=0,message=msg,status=status.HTTP_200_OK)                   
          else: 
               return response(condition=0,message=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
     serializer_class=AuthTokenSerializer
     def post(self,request):
          serializer=self.serializer_class(data=request.data)
          if(serializer.is_valid(raise_exception=True)):
               try:
                    user = Profile.objects.get(username=serializer.validated_data["username"])
                    if user.check_password(serializer.validated_data["password"]):
                         token,_=Token.objects.get_or_create(user=user)
                         msg="Token "+token.key
                         return response(condition=1,message=msg,status=status.HTTP_200_OK)
                         
                    else:
                         msg="pass word is incorrect"
                         return response(condition=0,message=msg,status=status.HTTP_400_BAD_REQUEST)
                    
               except Profile.DoesNotExist:
                    msg="user dosent exist"
                    return response(condition=0,message=msg,status=status.HTTP_400_BAD_REQUEST)
                                   
          else: 
               return response(condition=0,message=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


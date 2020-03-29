from django.shortcuts import render
from rest_framework.views import APIView
from  .serializer import RegisterSerializer,ChargingSerializer
from utils.Response import response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import Profile
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class Register(APIView):
     serializer_class=RegisterSerializer
     def post(self,request):
          serializer=self.serializer_class(data=request.data)
          if(serializer.is_valid()):
               serializer.save()
               msg="user "+request.data["username"]+" registerd successFully"
               return  response(condition=1,message=msg,status=status.HTTP_200_OK)                   
          else: 
               return response(condition=0,message=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
     serializer_class=AuthTokenSerializer
     def post(self,request):
          serializer=self.serializer_class(data=request.data)
          if(serializer.is_valid(raise_exception=True)):
               try:
                    user = Profile.objects.get(username=serializer.validated_data["username"])
                    print("......................",user.username)
                    if user.check_password(serializer.validated_data["password"]):
                         token,_=Token.objects.get_or_create(user=user)
                         msg={"Token":"Token "+token.key}
                         return response(condition=1,message=msg,status=status.HTTP_200_OK)
                         
                    else:
                         msg="pass word is incorrect"
                         return response(condition=0,message=msg,status=status.HTTP_400_BAD_REQUEST)
                    
               except Profile.DoesNotExist:
                    msg="user dosent exist"
                    return response(condition=0,message=msg,status=status.HTTP_400_BAD_REQUEST)
                                   
          else: 
               return response(condition=0,message=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ChargingAccount(APIView):
     serializer_class=ChargingSerializer
     permission_classes=[IsAuthenticated,]
     def patch(self,request):
          serializer=self.serializer_class(data=request.data)
          if(serializer.is_valid(raise_exception=True)):
               user=request.user
               money=serializer.validated_data["credit"]
               if money>=0:
                    user.credit+= money
                    user.save()
                    msg = "your account chrged succesFully new credit : "+str(user.credit)
                    return response(condition=1,message=msg,status=status.HTTP_200_OK)
               else:
                    msg = "creadit must be positive integer number "
                    return response(condition=0,message=msg,status=status.HTTP_400_BAD_REQUEST)
                          


          else:
               return response(condition=0,message=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
class GetMoney(APIView):
     serializer_class=ChargingSerializer
     permission_classes=[IsAuthenticated,]
     def patch(self,request):
          serializer=self.serializer_class(data=request.data)
          if(serializer.is_valid(raise_exception=True)):
               user=request.user
               money=serializer.validated_data["credit"]
               if money>=0:
                    if user.credit >= money:     
                         user.credit-= money
                         user.save()
                         msg = str(money)+"$ deposit on you banking account soon  your creadit : "+str(user.credit)
                         return response(condition=1,message=msg,status=status.HTTP_200_OK)                         

                    else:

                         msg = {
                              "message":"your request money is more than your  credit : ",
                              "request":money,
                              "creadit":user.credit
                         }

                         return response(condition=0,message=msg,status=status.HTTP_400_BAD_REQUEST)
                                        
               else:
                    msg = "creadit must be positive integer number "
                    return response(condition=0,message=msg,status=status.HTTP_400_BAD_REQUEST)
                          


          else:
               return response(condition=0,message=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class GetProfile(APIView):
     permission_classes=[IsAuthenticated,]
     def get(self,request):
          user=request.user
          credit=user.credit

          try:
              customer=user.customer
              usertype="customer"
          except:
               usertype = "Admin"


          msg = {
               "username":user.username,
               "credit":credit,
               "usertype":usertype

          }
          return response(condition=1, message=msg, status=status.HTTP_200_OK)
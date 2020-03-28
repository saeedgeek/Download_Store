from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from production import serializer
from utils.permissions import AdminPermission, CustomerPersmission
from rest_framework.views import APIView
from rest_framework import status
from utils.Response import response
from .models import Store
from .serializer import StoreSerializer,StoreListSerializer,StoreMemberShipSerializer
from django.utils import timezone
from user.models import StoreCustomer
from datetime import date
# Create your views here.

class Create(APIView):
     permission_classes=[AdminPermission,IsAuthenticated]
     serializer_class=StoreSerializer
     def post(self,request):
          serializer=self.serializer_class(data=request.data,context={"request":request})
          if serializer.is_valid():
               serializer.save()
               msg="the store with name ",serializer.validated_data['name']+ "create successFully"
               return response(condition=1,message=msg,status=status.HTTP_200_OK)
          else:
               return response(condition=0,message=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ListOfAdminStore(APIView):
     permission_classes=[AdminPermission,IsAuthenticated]
     def get(self,request):
          admin=request.user.admin
          stores=Store.objects.filter(admin=admin)
          serlilizer=StoreSerializer(stores,many=True)
          msg={"Stores list":serlilizer.data}
          return response(condition=1, message=msg, status=status.HTTP_200_OK)

class StoreList(APIView):
     serilizer_class=StoreListSerializer
     def get(self,request):
          stores=Store.objects.all()
          serlilizer=StoreSerializer(stores,many=True)
          msg={"Stores list":serlilizer.data}
          return response(condition=1, message=msg, status=status.HTTP_200_OK)


class BuyStoreMemberShip(APIView):
     permission_classes=[CustomerPersmission,IsAuthenticated]
     serializer_class=StoreMemberShipSerializer
     def post(self,request):
          serializer=self.serializer_class(data=request.data)
          if serializer.is_valid():
               store=serializer.validated_data["name"]
               store=Store.objects.get(name=store)
               Cuser=request.user
               customer=Cuser.customer
               customrt_stores=customer.store.all()
               if store in customrt_stores:
                    storeCustomer=StoreCustomer.objects.filter(store=store,customer=customer).get()
                    if storeCustomer.expire_time<date.today():
                         Cuser.credit -= store.price
                         auser = store.admin.user
                         auser.credit += store.price
                         Cuser.save()
                         auser.save()
                         now = timezone.now()
                         storeCustomer.expire_time=timezone.datetime(year=now.year+2,month=now.month,day=now.day)
                         storeCustomer.save()
                         msg = "membership Update successFully "
                         return response(condition=1, message=msg, status=status.HTTP_200_OK)
                    else:
                         msg="you  get membership of "+serializer.validated_data["name"] + " store before"
                         return response(condition=1, message=msg, status=status.HTTP_202_ACCEPTED)

               if customer.user.credit<store.price:
                    msg = "you  dont have enough money sharge your account"
                    return response(condition=0, message=msg, status=status.HTTP_402_PAYMENT_REQUIRED)


               Cuser.credit -= store.price
               auser=store.admin.user
               auser.credit += store.price
               Cuser.save()
               auser.save()
               now=timezone.now()
               expire_time=timezone.datetime(year=now.year+2,month=now.month,day=now.day)
               StoreCustomer.objects.create(customer=customer,store=store,expire_time=expire_time)
               customer.save()
               msg = "membership Buy successFully "
               return response(condition=1, message=msg, status=status.HTTP_200_OK)

          else:
               return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


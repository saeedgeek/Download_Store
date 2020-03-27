from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from utils.permissions import AdminPermission,CustomerPersmission
from rest_framework.views import APIView
from rest_framework import status
from utils.Response import response
from .models import Store
from .serializer import StoreSerializer
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


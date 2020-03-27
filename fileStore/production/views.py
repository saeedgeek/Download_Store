from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.permissions import IsAuthenticated
from utils.permissions import AdminPermission,StoreForThisAdmin
from .serializer import  CategourySerializer,ProductSerializer
from utils.Response import response
from rest_framework import status
from .models import  Category
# Create your views here.


class GetListOfCategory(APIView):
    def get(self,request):
        categories=Category.objects.all()
        serializer=CategourySerializer(categories,many=True)
        return response(condition=1, message={"list_of_categories":serializer.data}, status=status.HTTP_200_OK)


class CreateCategoury(APIView):
    permission_classes = (IsAuthenticated,AdminPermission)
    serializer_class=CategourySerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg="categoury "+serializer.validated_data["name"]+" create successFully"
            return response(condition=1, message=msg, status=status.HTTP_200_OK)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateProduct(APIView):
    permission_classes = (IsAuthenticated,AdminPermission,StoreForThisAdmin)
    serializer_class=ProductSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg="Product "+serializer.validated_data["name"]+" create successFully"
            return response(condition=1, message=msg, status=status.HTTP_200_OK)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


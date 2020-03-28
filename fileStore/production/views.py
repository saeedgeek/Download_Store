from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.permissions import IsAuthenticated
from utils.permissions import AdminPermission,StoreForThisAdmin,ProductForThisAdmin
from .serializer import CategourySerializer, ProductSerializer, ProductGetListSerializer, ProductShowListSerializer, \
    FileGetListSerializer, FileShowListSerializer, FileSerializer
from utils.Response import response
from rest_framework import status
from .models import  Category,File,Product
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

class ListOfStoreProduct(APIView):
    serializer_class=ProductGetListSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            store=serializer.validated_data["store"]
            products=Product.objects.filter(store=store)
            products=ProductShowListSerializer(products,many=True)
            msg={"products":products.data}
            return response(condition=1, message=msg, status=status.HTTP_200_OK)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListOfProductFiles(APIView):
    serializer_class=FileGetListSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data["product"]
            files = File.objects.filter(product=product)
            files = FileShowListSerializer(files, many=True)
            msg = {"Files": files.data}
            return response(condition=1, message=msg, status=status.HTTP_200_OK)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadFile(APIView):
    permission_classes = (IsAuthenticated,AdminPermission,ProductForThisAdmin)
    serializer_class=FileSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = "Files "+ serializer.validated_data["name"]+" upload successFully"
            return response(condition=1, message=msg, status=status.HTTP_200_OK)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


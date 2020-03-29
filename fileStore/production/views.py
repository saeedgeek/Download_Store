from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.permissions import IsAuthenticated

from user.models import Customer
from utils.permissions import AdminPermission, StoreForThisAdmin, ProductForThisAdmin, CustomerPersmission
from .serializer import CategourySerializer, ProductSerializer, ProductGetListSerializer, ProductShowListSerializer, \
    FileGetListSerializer, FileShowListSerializer, FileSerializer, BuyDownloadFileSerializer, \
    BuyDownloadFileProducterializer
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



class BuyProduct(APIView):
    serializer_class= BuyDownloadFileProducterializer
    permission_classes = (IsAuthenticated,CustomerPersmission)
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            Ucustomer=request.user
            customer=Ucustomer.customer

            productRequested=serializer.validated_data["id"]
            try:
                productRequested=Product.objects.get(id=serializer.validated_data["id"])
            except:
                msg = "this Product is not exist"
                return response(condition=0, message=msg, status=status.HTTP_400_BAD_REQUEST)
            customerProduct=customer.product.all()
            Uadmin=productRequested.store.admin.user
            if productRequested in customerProduct:
                msg = "you  Buy " + str(serializer.validated_data["id"]) + " Product before"
                return response(condition=1, message=msg, status=status.HTTP_202_ACCEPTED)
            elif productRequested.fee > Ucustomer.credit:
                msg = "you  dont have enough money sharge your account"
                return response(condition=0, message=msg, status=status.HTTP_402_PAYMENT_REQUIRED)
            else:
                Uadmin.credit+=productRequested.fee
                Ucustomer.credit -= productRequested.fee
                customer.product.add(productRequested)
                customer.save()
                Ucustomer.save()
                Uadmin.save()
                msg = "Product Buy successFully "
                return response(condition=1, message=msg, status=status.HTTP_200_OK)


        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuyFile(APIView):
    serializer_class=BuyDownloadFileSerializer
    permission_classes = (IsAuthenticated,CustomerPersmission)

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        pass
        if serializer.is_valid():
            Ucustomer=request.user
            customer=Customer.objects.prefetch_related("product").prefetch_related("_file").get(user=Ucustomer)
            filerequested=None
            try:
                filerequested=File.objects.get(id=serializer.validated_data["id"])
            except:
                msg = "this File is not exist"
                return response(condition=0, message=msg, status=status.HTTP_400_BAD_REQUEST)
            Uadmin=filerequested.product.store.admin.user
            customer_file_list=customer._file.all()
            customer_product_file=[]
            for product in customer.product.all():
                customer_product_file.append(list(product.file))
            customer_all_file=list(customer_file_list)+customer_product_file
            if filerequested in customer_all_file:
                msg = "you  Buy " + str(serializer.validated_data["id"]) + " File before"
                return response(condition=1, message=msg, status=status.HTTP_202_ACCEPTED)
            elif filerequested.fee > Ucustomer.credit:
                msg = "you  dont have enough money sharge your account"
                return response(condition=0, message=msg, status=status.HTTP_402_PAYMENT_REQUIRED)
            else:
                Uadmin.credit+=filerequested.fee
                Ucustomer.credit -= filerequested.fee
                customer._file.add(filerequested)
                customer.save()
                Ucustomer.save()
                Uadmin.save()
                msg = "File Buy successFully "
                return response(condition=1, message=msg, status=status.HTTP_200_OK)



        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)









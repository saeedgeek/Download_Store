from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from utils.permissions import AdminPermission,CustomerPersmission
from rest_framework.views import APIView
from rest_framework import status
from utils.Response import response
from .models import Store
# Create your views here.


class Create(APIView):
     permission_classes=[AdminPermission,IsAuthenticated]
     def post(self,request):

          return response(1,"hasperm",status.HTTP_200_OK)


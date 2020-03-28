from rest_framework.permissions import BasePermission

from production.models import Product
from user.models import Admin,Customer
from store.models import Store

class AdminPermission(BasePermission):
     def has_permission(self, request, view):
          try:
               admin=Admin.objects.get(user=request.user)
               if admin:
                    return True
               else:
                    return False     
          except:
               return False

class StoreForThisAdmin(BasePermission):
     def has_permission(self, request, view):
          try:
               store_requested=request.data["store"]
               admin=request.user.admin
               stores=Store.objects.filter(admin=admin)
               list_of_store_name=[]
               for store in stores:
                    list_of_store_name.append(store.name)
               print(list_of_store_name)
               print(store_requested)
               if store_requested in list_of_store_name:
                    return True
               else:
                    return False
          except:
               return False



class CustomerPersmission(BasePermission):
    def has_permission(self, request, view):
          try:
               customer=Customer.objects.get(user=request.user)
               if customer:
                    return True
               else:
                    return False
          except:
               return False


class ProductForThisAdmin(BasePermission):
     def has_permission(self, request, view):
          try:
               request_product=request.data["product"]
               request_product=Product.objects.get(id=request_product)
               admin=request.user.admin
               AdminStores=Store.objects.filter(admin=admin).prefetch_related("product")
               list_of_admin_product=[]
               for store in AdminStores:
                    list_of_admin_product += store.product.all()
               if request_product in list(list_of_admin_product):

                    return  True
               else:

                    return False
          except:
               return False

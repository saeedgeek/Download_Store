from rest_framework.permissions import BasePermission
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
               admin=Admin.objects.get(user=request.user)
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
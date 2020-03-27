from rest_framework.permissions import BasePermission
from user.models import Admin,Customer


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
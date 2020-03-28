from django.urls import path
from .views import Create,ListOfAdminStore,StoreList,BuyStoreMemberShip
urlpatterns = [
path("create_store",Create.as_view()),
path("list_of_admin_store", ListOfAdminStore.as_view()),
path("store_list", StoreList.as_view()),
path("buy_member_ship", BuyStoreMemberShip.as_view()),

]

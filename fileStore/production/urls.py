from django.urls import path
from .views import CreateCategoury, GetListOfCategory, CreateProduct, ListOfStoreProduct, ListOfProductFiles, \
    UploadFile, BuyFile,BuyProduct,GetUserResource

urlpatterns = [
path("create_categouri",CreateCategoury.as_view()),
path("create_product",CreateProduct.as_view()),
path("list_of_categories",GetListOfCategory.as_view()),
path("list_of_store_products",ListOfStoreProduct.as_view()),
path("list_of_product_files",ListOfProductFiles.as_view()),
path("upload_File",UploadFile.as_view()),#
path("buy_file", BuyFile.as_view()),
path("buy_product", BuyProduct.as_view()),
path("get_user_resource", GetUserResource.as_view()),

]

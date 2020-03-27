from django.urls import path
from .views import CreateCategoury,GetListOfCategory,CreateProduct,ListOfStoreProduct,ListOfProductFiles
urlpatterns = [
path("create_categouri",CreateCategoury.as_view()),
path("create_product",CreateProduct.as_view()),
path("list_of_categories",GetListOfCategory.as_view()),
path("list_of_store_product",ListOfStoreProduct.as_view()),
path("list_of_product_files",ListOfProductFiles.as_view())
]

from django.urls import path
from .views import CreateCategoury,GetListOfCategory
urlpatterns = [
path("create_categouri",CreateCategoury.as_view()),
path("list_of_categories",GetListOfCategory.as_view())
]

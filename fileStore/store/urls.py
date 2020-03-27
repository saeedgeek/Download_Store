from django.urls import path
from .views import Create,ListOfAdminStore
urlpatterns = [
path("create_store",Create.as_view()),
path("list_of_admin_store", ListOfAdminStore.as_view()),
]

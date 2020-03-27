from django.urls import path
from .views import Create
urlpatterns = [
 path("create_store",Create.as_view())
]

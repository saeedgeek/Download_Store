from django.urls import path
from .views import Register,Login,ChargingAccount
urlpatterns = [
    path("register",Register.as_view()),
    path("login",Login.as_view()),
    path("charge_account",ChargingAccount.as_view()),
]

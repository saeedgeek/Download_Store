from django.urls import path
from .views import Register,Login,ChargingAccount,GetMoney,GetProfile
urlpatterns = [
    path("register",Register.as_view()),
    path("login",Login.as_view()),
    path("charge_account",ChargingAccount.as_view()),
    path("get_money",GetMoney.as_view()),
    path("get_profile",GetProfile.as_view()),
]

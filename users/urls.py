from django.urls import path
from .apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView


app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

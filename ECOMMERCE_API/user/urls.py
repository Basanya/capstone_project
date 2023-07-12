from django.urls import path
from .views import home, my_login,register

urlpatterns = [
    path("homi/", home,name="home"),
    path("login/", my_login, name="log"),
    path("reg/", register, name="regg")
]
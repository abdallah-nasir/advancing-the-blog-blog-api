from django.urls import path,include
from . import views
from .views import *

app_name ="accounts"
urlpatterns = [
path("register",CreateUserApiView.as_view(),name="create_user"),
path("login",UserLoginApiView.as_view(),name="login_user"),

]
  



  
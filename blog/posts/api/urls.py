from django.urls import path,include
from . import views
from .views import *

app_name ="post"
urlpatterns = [
path("list",PostListAPiView.as_view(),name="list"),
path("create",PostCreateApiView.as_view(),name="create"),
path("details/<str:slug>",PostDetailApiView.as_view(),name="detail"),
path("update/<str:slug>",PostUpdateApiView.as_view(),name="update"),
path("delete/<str:slug>",PostDeleteApiView.as_view(),name="delete"),
path("comments",CommentListAPiView.as_view(),name="comments"),
path("comments/detail/<id>",CommentDetailAPiView.as_view(),name="comment_detail"),
path("comments/update/<id>",CommentUpdateApiView.as_view(),name="comment_update"),
path("comments/delete/<id>",CommentDeleteApiView.as_view(),name="comment_delete"),


]
  
  

  
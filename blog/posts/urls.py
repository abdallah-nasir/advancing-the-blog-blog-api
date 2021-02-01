from django.urls import path,include
from . import views


app_name ="post"
urlpatterns = [
    path("create/",views.post_create,name="post"),
    path("details/<str:slug>/",views.post_detail,name="details"),
    path("list/",views.post_list,name="list"),
    path("update/<str:slug>/",views.post_update,name="update"),
    path("delete/<str:slug>/",views.post_delete,name="delete"),
    path("delete_comment/<str:slug>/<id>/",views.comment_delete,name="comment_delete"),
    path("comment_page/<str:slug>/<id>/",views.comment_page,name="comment_page"),


]
  
  

  
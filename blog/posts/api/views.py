from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import(
ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView,
RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permissions import *
from .serializers import *
from posts.models import Post
from .pagination import *

class PostCreateApiView(CreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostCreateSerializers
    permission_classes= [IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class PostDetailApiView(RetrieveAPIView):
    queryset= Post.objects.all()
    serializer_class = PostDetailSerializers
    permission_classes= [IsAuthenticated]

    lookup_field="slug"

class PostUpdateApiView(RetrieveUpdateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostDetailSerializers
    permission_classes= [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    lookup_field="slug"
   # def perform_update(self,serializer):
    #    serializer.save(user=self.request.user)

class PostDeleteApiView(DestroyAPIView):
    queryset= Post.objects.all()
    serializer_class = PostDetailSerializers
    permission_classes= [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    lookup_field="slug"

 
 
class PostListAPiView(ListAPIView):
    queryset= Post.objects.all()
    serializer_class = PostListSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['body', 'title']
    pagination_class = CustomPagination


class CommentListAPiView(ListAPIView):
    queryset= Comments.objects.filter(reply=None)
    serializer_class = CommentListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post', 'content']
    pagination_class = CustomPagination

class CommentDetailAPiView(RetrieveAPIView):
    queryset= Comments.objects.all()
    serializer_class = CommentDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post', 'content']
    pagination_class = CustomPagination
    lookup_field = "id"
    many= True

'''
class CommentCreateApiView(CreateAPIView):
    queryset= Comments.objects.all()
    serializer_class = CommentCreateSerializers
    permission_classes= [IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user,post=self.Post)
'''

class CommentUpdateApiView(RetrieveUpdateAPIView):
    queryset= Comments.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes= [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    lookup_field = "id"

class CommentDeleteApiView(DestroyAPIView):
    queryset= Comments.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes= [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    lookup_field="id"

 







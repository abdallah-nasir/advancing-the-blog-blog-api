from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from django.contrib.auth import get_user_model
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

from posts.api.permissions import *
from .serializers import *
from accounts.models import *
from posts.api.pagination import *

User = get_user_model() 


class CreateUserApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer 

class UserLoginApiView(APIView):
    permission_classes= [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self,request,*args,**kwargs):
        data = request.data #  ==request.POST
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            new_data = serializer.data
            return Response(new_data,status=HTTP_200_OK)
        else:       
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)



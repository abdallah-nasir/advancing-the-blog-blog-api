from rest_framework.serializers import ( ModelSerializer,
HyperlinkedIdentityField,SerializerMethodField)
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.exceptions import ValidationError
from posts.models import Post,Comments

post_detail_url = HyperlinkedIdentityField(view_name='api:detail',lookup_field="slug")
post_delete_url = HyperlinkedIdentityField(view_name='api:delete',lookup_field="slug")

User = get_user_model() 


class UserCreateSerializer(ModelSerializer):
    email = serializers.EmailField(label="Email Address")
    email2 = serializers.EmailField(label="Confirm Email")
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","email2","password"]
        extra_kwargs={"password":
                    {"write_only":True}
        }

    def validate_email2(self,value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Email must be the Same !")
        return value


    def validate_email(self,value):
        data = self.get_initial()
        email1 = data.get("email")
        user_qs = User.objects.filter(email=email1)
        if user_qs.exists():
            raise ValidationError("Email Address is Already exist")
        return value


    def create(self,validated_data):
        username= validated_data["username"]
        first_name= validated_data["first_name"] 
        last_name = validated_data["last_name"]
        password = validated_data["password"]
        email = validated_data["email"]
        user_obj = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email= email,
        ) 

        user_obj.set_password(password),
        user_obj.save() 
        return validated_data




class UserLoginSerializer(ModelSerializer):
    email = serializers.EmailField(label="Email Address")
    token = serializers.CharField(allow_blank=True,read_only=True)
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ["username","email","password","token"]
        extra_kwargs={"password":
                    {"write_only":True}
        }


    def validate(self,data):
        email = data.get("eamil")
        username= data.get("username")
        if not email and not username:
            raise ValidationError("Username or Email are Required")


        return data
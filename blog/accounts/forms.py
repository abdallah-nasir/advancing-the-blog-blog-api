from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username or Password Might be WRONG")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class SignupForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    email2 =forms.EmailField(label="Confirm Email")
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","email2",'password1']

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        email = cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("this Email is Already Signed in")
        email2 = cleaned_data.get("email2")
        if email != email2:
            raise ValidationError("Email Field Must be The Same")
        return cleaned_data


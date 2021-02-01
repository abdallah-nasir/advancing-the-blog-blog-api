from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.contrib.auth.forms import UserCreationForm
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
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class SignupForm(UserCreationForm):   
    email2=forms.EmailField(label="Confirm Email")
    email= forms.EmailField(label="Email Address")
    class Meta:
        model = User
        fields = ['username',"first_name","last_name",'email',"email2",'password1','password2']

    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email Already Exists")
        if email != email2:
            raise forms.ValidationError("Email Dosn't match")
        return super(SignupForm,self).clean(*args,**kwargs)


    def clean_email2(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email Already Exists")
        if email != email2:
            raise forms.ValidationError("Email Dosn't match")
        return email

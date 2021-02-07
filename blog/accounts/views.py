from django.shortcuts import render,redirect,Http404
from django.contrib.auth import (
    authenticate,get_user_model,login,logout
)

from .forms import *
from .decorators import notLoggedUsers
from django.contrib import messages

# Create your views here.

@notLoggedUsers
def login_view(request):
    form = UserLoginForm(request.POST or None)
    next= request.GET.get("next")
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect("/list")
    context={"form":form}
    return render(request,"login.html",context)


def register_view(request):
    next=request.GET.get("next")
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid():  
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username,password=password)
            login(request,user)
            if next:
                return redirect(next)
            return redirect("/list")
    else:
        form = SignupForm()
    context={"form":form}
    return render(request,"register.html",context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        raise Http404
    context={}
    return render(request,"logout.html",context)
from django.shortcuts import render,redirect,Http404
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from .models import *
from .forms import *
from .filters import *

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/") #you can you settings to make a default login 
def post_create(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request,"Post Created Successfully")
        return redirect(reverse("home:details",kwargs={"slug":instance.slug}))

 #   if request.method =="POST":
  #      print("content is " + request.POST.get("content"))
    context={"form":form}
    return render(request,"post_form.html",context)
 


def post_detail(request,slug):          #retrive
    instance = Post.objects.get(slug=slug)
    comments = Comments.objects.filter(post=instance,reply=None).order_by("-id")
    if request.method =="POST":
        form = CommentForm(request.POST or None,instance=instance)
        if form.is_valid():
            content = request.POST.get("content")
            reply_id = request.POST.get("comment_id")
            comment_qs = None 
            if reply_id:
                comment_qs = Comments.objects.get(id=reply_id)
            comment = Comments.objects.get_or_create(post=instance, user=request.user,content=content,reply=comment_qs)
            form.save()
            return redirect(reverse("home:details",kwargs={"slug":instance.slug}))
           
    else:
        form=CommentForm(None)
    context ={"instance":instance,"comments":comments,"form":form}
    return render(request,"post_detail.html",context)



def post_list(request):          #list items
    instance = Post.objects.all()

    post_filter = PostFilter(request.GET,queryset=instance)
    instance = post_filter.qs 

    paginator = Paginator(instance,4) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={"objects":page_obj,"myfilter":instance}
    return render(request,"post_list.html",context)

@login_required(login_url="/login/")
def post_update(request,slug):
    instance = Post.objects.get(slug=slug)
    form = PostForm(request.POST or None,request.FILES or None,instance=instance)
    if instance.user != request.user:
        raise Http404
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"updated")
        return redirect(reverse("home:details",kwargs={"slug":slug}))
    context ={"instance":instance,"form":form}
    return render(request,"post_form.html",context)

def post_delete(request,slug):
    instance = Post.objects.get(slug=slug)
    if instance.user != request.user:
        raise Http404
    if request.method =="POST":
        instance.delete()
        return redirect("/list")
    context = {"instance":instance}
    return render(request,"post_delete.html",context)

@login_required(login_url="/login/")
def comment_delete(request,id,slug):
    instance = Comments.objects.get(id=id)
    post = Post.objects.get(slug=instance.post.slug)
    if instance.user != request.user:
        raise Http404
    if request.method =="POST":
        instance.delete()
        return redirect(reverse("home:details",kwargs={"slug":post.slug}))
    context = {"instance":instance} 
    return render(request,"comment_delete.html",context)

@login_required(login_url="/login/")
def comment_page(request,id,slug):
    instance = Comments.objects.get(id=id)
    post = Post.objects.get(slug=instance.post.slug)
    comments = Comments.objects.filter(post=post ).order_by("-id")
    if request.method =="POST":
        form = CommentForm(request.POST or None,instance=post)
        if form.is_valid():
            content = request.POST.get("content")
            reply_id = request.POST.get("comment_id")
            comment_qs = None 
            if reply_id:
                comment_qs = Comments.objects.get(id=reply_id)
            comment = Comments.objects.get_or_create(post=post, user=request.user,content=content,reply=comment_qs)
            form.save()
            return redirect(reverse("home:comment_page",kwargs={"id":instance.id,"slug":instance.post.slug}))
           
    else:
        form=CommentForm(None)
    context = {"comments":comments,"form":form,"instance":instance} 
    return render(request,"comment_page.html",context)







    

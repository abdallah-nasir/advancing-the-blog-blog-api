from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","body","image"]


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea,label="")
    class Meta:
        model = Comments
        fields = ["content"]














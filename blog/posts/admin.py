from django.contrib import admin
from .models import *
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["updated","title","timestamp"] 
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["timestamp","title"]
    search_fields = ["content"]
    view_on_site = True
    class Meta:
        model = Post

admin.site.register(Post,PostModelAdmin)

admin.site.register(Comments)

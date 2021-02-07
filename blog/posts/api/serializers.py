from rest_framework.serializers import ( ModelSerializer,
HyperlinkedIdentityField,SerializerMethodField)

from rest_framework import serializers

from posts.models import Post,Comments

post_detail_url = HyperlinkedIdentityField(view_name='api:detail',lookup_field="slug")
post_delete_url = HyperlinkedIdentityField(view_name='api:delete',lookup_field="slug")


class PostCreateSerializers(ModelSerializer): # == models.Model
    class Meta:
        model = Post       
        fields=["title","body","image"]

class PostDetailSerializers(ModelSerializer): # == models.Model
    user= SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post       
        fields=["user","title","body","image","comments"]
    def get_user(self,obj):
        return str(obj.user.first_name+" "+obj.user.last_name).title()

    def get_comments(self,obj):
        return obj.comments.filter(reply=None).count()


class PostListSerializers(ModelSerializer): # == models.Model
    detail_url =post_detail_url
    delete_url=post_delete_url
    user = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post       
        fields=["user","title","comments","timestamp","detail_url","delete_url"]

    def get_user(self,obj):
        return str(obj.user.first_name+" "+obj.user.last_name).title()
    
    def get_comments(self,obj):
        return obj.comments.filter(reply=None).count()
    



comment_detial_url = HyperlinkedIdentityField(view_name="api:comment_detail",lookup_field="id")
class CommentListSerializer(ModelSerializer):
    post = SerializerMethodField()
    user = SerializerMethodField()
    url = comment_detial_url
    class Meta:
        model = Comments
        fields = ["post","user","content","url"]

    def get_post(self,obj):
        return str(obj.post.title)

    def get_user(self,obj):
        return str(obj.user.first_name+" "+obj.user.last_name).title()
    
class RepliesSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Comments
        fields = ["user","content"]

    def get_user(self,obj):
        return str(obj.user.first_name+" "+obj.user.last_name).title()

comment_update_url = HyperlinkedIdentityField(view_name="api:comment_update",lookup_field="id")
comment_delete_url = HyperlinkedIdentityField(view_name="api:comment_delete",lookup_field="id")


class CommentDetailSerializer(ModelSerializer):
    post = SerializerMethodField()
    user = SerializerMethodField()
    replies = SerializerMethodField()
    ReplyCount = SerializerMethodField()
    update_url = comment_update_url
    delte_url = comment_delete_url
    class Meta:
        model = Comments
        fields = ["post","user","content","update_url","delte_url","ReplyCount","replies"]

    def get_post(self,obj):
        return str(obj.post.title)

    def get_user(self,obj):
        return str(obj.user.first_name+" "+obj.user.last_name).title()
    

    def get_replies(self,obj):
        replies = RepliesSerializer(obj.replies,many=True).data
        return replies

    def get_ReplyCount(self,obj):
        return obj.replies.count()
'''
class CommentCreateSerializers(ModelSerializer): # == models.Model
    class Meta:
        model = Comments       
        fields=["content"]
'''



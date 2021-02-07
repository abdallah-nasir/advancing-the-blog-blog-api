from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .utils import unique_slug_generator
from ckeditor.fields import RichTextField
# Create your models here.


def upload_location(instance,filename):
    filebase,extension = filename.split(".")
    return "%s/%s.%s" %(instance.title,instance.title,extension)

class Post(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    body = RichTextField(blank=True,null=True)
  #  content = models.TextField() 
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    image = models.ImageField(upload_to=upload_location,null=True, blank=True,default="index.png")
    slug = models.SlugField(null=True,unique=True,blank=True)
    

    def __str__(self):
        return self.title

    def post_count(user):
        return Post.objects.filter(user=user).count()

    class Meta:
        ordering =["-timestamp"] 


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Post)
'''
    def save(self,*args,**kwargs):
        if Post.objects.filter(title=self.title).exists():
            unique_slug = str(self.user.id)
            self.slug = slugify(self.title)+"-"+unique_slug
            save() 
        else:
            self.slug = slugify(self.title) 
        super(Post,self).save(*args,**kwargs)
'''
class Comments(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    content = models.TextField()
    reply = models.ForeignKey("Comments", null= True, related_name="replies",on_delete=models.CASCADE)  
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

     

    def __str__(self):
        return self.post.title


'''
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists() 
    if exists:
        slug = "%s-%s"%(slug,instance.id)
    instance.slug = slug

pre_save.connect(pre_save_post_receiver,sender=Post)
'''




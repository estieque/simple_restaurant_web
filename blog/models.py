from distutils.command.upload import upload
from email import message
from django.db import models
from django.utils.html import format_html
from django.template.defaultfilters import slugify
# Create your models here.

class PostAuthor(models.Model):
    auth_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    image = models.ImageField(upload_to='authimage/')
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
        
        

class PostCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=80)
    meta_tags = models.CharField(max_length=200)
    description =models.TextField()
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
         
        
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=155)
    meta_tags = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(upload_to='blogimage/')
    cat = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(PostAuthor,null=True, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ("add_date",)
    def __str__(self):
        return '%s - %s' % (self.post.slug, self.name)
        
    
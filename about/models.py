from django.db import models
from django.utils.html import format_html
# Create your models here.
class TeamMember(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='team/')
    designation = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    
    def __str__(self):
        return self.name
    
class AboutContent(models.Model):
    content_id = models.AutoField(primary_key=True)
    small_description = models.CharField(max_length=400)
    content = models.TextField()
    
    def __str__(self):
        return self.small_description
        
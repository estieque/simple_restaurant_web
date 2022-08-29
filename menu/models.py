from django.db import models
from django.utils.html import format_html
# Create your models here.

    

    
class breakfastMenu(models.Model):
    
    menu_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    ratings = models.CharField(max_length=100)
    total_reviews = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menuimage/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
class launchMenu(models.Model):
    
    menu_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    ratings = models.CharField(max_length=100)
    total_reviews = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menuimage/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
class dinnerMenu(models.Model):
    
    menu_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    ratings = models.CharField(max_length=100)
    total_reviews = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menuimage/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
    
    
class specialMenu(models.Model):
    s_id = models.AutoField(primary_key=True)
    breakfast = models.ForeignKey(breakfastMenu, on_delete=models.CASCADE)
    launch = models.ForeignKey(launchMenu, on_delete=models.CASCADE)
    dinner = models.ForeignKey(dinnerMenu, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %s' % (self.breakfast, self.launch)
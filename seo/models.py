from turtle import title
from django.db import models

# Create your models here.


class HomePage(models.Model):
    title = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    meta_description = models.TextField()
    class Meta:
        verbose_name_plural = "Home Page Meta Tags"
    def __str__(self):
        return self.title
    
    
class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    meta_description = models.TextField()
    class Meta:
        verbose_name_plural = "About Page Meta Tags"
    def __str__(self):
        return self.title
    
    
class BlogPage(models.Model):
    title = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    meta_description = models.TextField()
    class Meta:
        verbose_name_plural = "Blog Page Meta Tags"
    def __str__(self):
        return self.title
    
    
class MenuPage(models.Model):
    title = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    meta_description = models.TextField()
    class Meta:
        verbose_name_plural = "Menu Page Meta Tags"
    def __str__(self):
        return self.title
    
    
class ContactPage(models.Model):
    title = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    meta_description = models.TextField()
    class Meta:
        verbose_name_plural = "Contact Page Meta Tags"
    def __str__(self):
        return self.title
from django.db import models
from django.utils.html import format_html
# Create your models here.
class homeSliderOne(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=60, null=True)
    ratings = models.CharField(max_length=60, null=True)
    image = models.ImageField(upload_to='slideimage/')
    
    class Meta:
        verbose_name_plural = "Home Slider One"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
    
class homeSliderTwo(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=60, null=True)
    ratings = models.CharField(max_length=60, null=True)
    image = models.ImageField(upload_to='slideimage/')
    
    class Meta:
        verbose_name_plural = "Home Slider Two"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
        
class homeSliderThree(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=60, null=True)
    ratings = models.CharField(max_length=60, null=True)
    image = models.ImageField(upload_to='slideimage/')
    
    class Meta:
        verbose_name_plural = "Home Slider Three"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name

class storySlider(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideimage/')
    
    class Meta:
        verbose_name_plural = "Story Slider"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
    
    
class menuSlider(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideimage/')
    class Meta:
        verbose_name_plural = "Menu Slider"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
    
class blogSlider(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideimage/')
    
    class Meta:
        verbose_name_plural = "Blog Slider"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
    
class contactSlider(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideimage/')
    class Meta:
        verbose_name_plural = "Contact Slider"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
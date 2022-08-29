from django.db import models

# Create your models here.
from django.db import models

# Create your models here.




from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    meta_description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(blank=True, null=True, max_length=50)
    logo = models.ImageField(blank=True, null=True, upload_to='icon/')
    favicon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    linkedIn = models.CharField(blank=True, max_length=100)
    twitter = models.CharField(blank=True, max_length=100)
    address = models.TextField()
    contact = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title






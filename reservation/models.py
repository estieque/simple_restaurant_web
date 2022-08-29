from email import message
from django.db import models

# Create your models here.
class Reservation(models.Model):
    reserve_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    total_person = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    message = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.name
from django.contrib import admin

from contact.models import ContactMessage

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name',)
    
admin.site.register(ContactMessage, ContactMessageAdmin)
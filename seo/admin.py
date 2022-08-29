from django.contrib import admin

from seo.models import *

# Register your models here.
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_keyword', 'meta_description',)
    search_fields = ('title',)
    
    
admin.site.register(HomePage,HomePageAdmin)



class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_keyword', 'meta_description',)
    search_fields = ('title',)
    
    
admin.site.register(AboutPage,AboutPageAdmin)


class BlogPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_keyword', 'meta_description',)
    search_fields = ('title',)
    
    
admin.site.register(BlogPage,BlogPageAdmin)

class MenuPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_keyword', 'meta_description',)
    search_fields = ('title',)
    
    
admin.site.register(MenuPage,MenuPageAdmin)


class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_keyword', 'meta_description',)
    search_fields = ('title',)
    
    
admin.site.register(ContactPage,ContactPageAdmin)
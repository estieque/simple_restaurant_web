from email.headerregistry import Group
from django.contrib import admin
from .models import Comment, PostCategory, BlogPost, PostAuthor
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from django_summernote.models import Attachment
from django.contrib.auth.models import Group


admin.site.unregister(Attachment)
admin.site.unregister(Group)

class PostAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(PostAuthor, PostAuthorAdmin)

class PostCategoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'meta_description', 'slug', 'image_tag', 'add_date')
    search_fields = ('title',)
    summernote_fields = ('description',)
    list_per_page = 10


admin.site.register(PostCategory, PostCategoryAdmin)

class BlogpostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'image_tag', 'add_date')
    search_fields = ('title',)
    summernote_fields = ('content',)
    list_per_page = 10



admin.site.register(BlogPost, BlogpostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content',)
    search_fields = ('name', 'email',)

admin.site.register(Comment, CommentAdmin)
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from about.models import AboutContent, TeamMember

# Register your models here.
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'designation', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(TeamMember, TeamMemberAdmin)


class AboutContentAdmin(SummernoteModelAdmin):
    list_display = ('small_description',)
    summernote_fields = ('content',)
    
admin.site.register(AboutContent, AboutContentAdmin)
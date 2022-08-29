from django.contrib import admin

from menu.models import breakfastMenu, dinnerMenu, launchMenu, specialMenu

# Register your models here.




class specialMenuAdmin(admin.ModelAdmin):
    list_display = ('breakfast', 'launch', 'dinner',)
    
    
admin.site.register(specialMenu, specialMenuAdmin)

class breakfastMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'price', 'ratings',)
    search_fields = ('title',)
    
admin.site.register(breakfastMenu, breakfastMenuAdmin)

class launchMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'price', 'ratings',)
    search_fields = ('title',)
    
admin.site.register(launchMenu, launchMenuAdmin)

class dinnerMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'price', 'ratings',)
    search_fields = ('title',)
    
admin.site.register(dinnerMenu, dinnerMenuAdmin)
from django.contrib import admin

from sliders.models import blogSlider, contactSlider, homeSliderOne, homeSliderThree, homeSliderTwo, menuSlider, storySlider

# Register your models here.
class homeSliderOneAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'ratings')
    search_fields = ('name',)
    
admin.site.register(homeSliderOne, homeSliderOneAdmin)

class homeSliderTwoAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'ratings')
    search_fields = ('name',)
    
admin.site.register(homeSliderTwo, homeSliderTwoAdmin)

class homeSliderThreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'ratings')
    search_fields = ('name',)
    
admin.site.register(homeSliderThree, homeSliderThreeAdmin)

class storySliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(storySlider, storySliderAdmin)

class blogSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(blogSlider, blogSliderAdmin)

class menuSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(menuSlider, menuSliderAdmin)

class contactSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(contactSlider, contactSliderAdmin)
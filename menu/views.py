from multiprocessing import context
from django.shortcuts import render
from menu.models import breakfastMenu, dinnerMenu, launchMenu

from restaurantWeb.models import SiteSetting
from seo.models import MenuPage
from sliders.models import menuSlider

# Create your views here.
def menu(request):
    settings = SiteSetting.objects.all()
    breakfast = breakfastMenu.objects.all()
    launch = launchMenu.objects.all()
    dinner = dinnerMenu.objects.all()
    menuseo = MenuPage.objects.all().order_by('-id')[:1]
    menuslider = menuSlider.objects.all().order_by('-hslider_id')[:1]
    context ={'settings':settings,'breakfast':breakfast, 'launch':launch, 'dinner':dinner, 'menuseo':menuseo,'menuslider':menuslider,}
    return render(request,'menu.html',context)
    
from multiprocessing import context
from django.shortcuts import render
from blog.models import BlogPost
from menu.models import specialMenu
from reservation.models import Reservation
from seo.models import HomePage

from sliders.models import homeSliderOne, homeSliderThree, homeSliderTwo
from .models import SiteSetting

# Create your views here.
def home(request):
    settings = SiteSetting.objects.all()
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    homesliderone = homeSliderOne.objects.all().order_by('-hslider_id')[:1]
    homeslidertwo = homeSliderTwo.objects.all().order_by('-hslider_id')[:1]
    homesliderthree = homeSliderThree.objects.all().order_by('-hslider_id')[:1]
    homeseo = HomePage.objects.all().order_by('-id')[:1]
    smenu = specialMenu.objects.all()
    
    context={'smenu':smenu, 'homeblogs':homeblogs, 'homesliderone':homesliderone, 'homeslidertwo':homeslidertwo, 'homesliderthree':homesliderthree, 'settings':settings,'homeseo':homeseo,}
    return render(request, 'index.html', context)
    
    
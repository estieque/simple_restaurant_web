from email import message
from django.shortcuts import render

from restaurantWeb.models import SiteSetting
from .models import Reservation
# Create your views here.
def reservedone(request):
    settings = SiteSetting.objects.all()
    context={'settings':settings,}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        total_person=request.POST.get('people')
        date=request.POST.get('date')
        time=request.POST.get('time')
        message=request.POST.get('message')
        en=Reservation(name=name,email=email,message=message,phone=phone,total_person=total_person,date=date,time=time)
        en.save()
    return render(request, "reservation.html",context)
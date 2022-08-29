from django.shortcuts import render
from contact.models import ContactMessage
from restaurantWeb.models import SiteSetting
from django.contrib import messages

from seo.models import ContactPage
from sliders.models import contactSlider
# Create your views here.
def contact(request):
    
    settings = SiteSetting.objects.all()
    contactseo = ContactPage.objects.all().order_by('-id')[:1]
    contactslider = contactSlider.objects.all().order_by('-hslider_id')[:1]
    context ={'settings':settings, 'contactseo':contactseo, 'contactslider':contactslider,}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        en=ContactMessage(name=name,email=email,message=message,phone=phone,)
        en.save()
        messages.success(request, 'Your Message Sent Sucessfully')
    return render(request,'contact.html',context)
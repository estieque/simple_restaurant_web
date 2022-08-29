from django.shortcuts import render
from django.contrib import messages
from emailsubs.models import EmailSubs
from restaurantWeb.models import SiteSetting
from rest_framework import viewsets

from seo.models import AboutPage
from sliders.models import storySlider
#from .serializers import TeamMemberSerializer
from .models import AboutContent, TeamMember
import requests
# Create your views here.





#class TeamMemberViewSet(viewsets.ModelViewSet):
   # queryset = TeamMember.objects.all()
    #serializer_class = TeamMemberSerializer
    
#from rest_framework.renderers import TemplateHTMLRenderer
#from rest_framework.response import Response
#from rest_framework.views import APIView
#from . import generics

#class UserDetail(generics.RetrieveAPIView):
    #"""
    #A view that returns a templated HTML representation of a given user.
    #"""
    #queryset = TeamMember.objects.all()
    #renderer_classes = [TemplateHTMLRenderer]

    #def get(self, request, *args, **kwargs):
        #self.object = self.get_object()
        #return Response({'team': self.object}, template_name='about.html')
 
    
def about(request):
    settings = SiteSetting.objects.all()
    #response = requests.get('http://127.0.0.1:2000/about/posts/')
    #team = response.json()
    team = TeamMember.objects.all()
    acontent = AboutContent.objects.all()
    aboutseo = AboutPage.objects.all().order_by('-id')[:1]
    aboutslider = storySlider.objects.all().order_by('-hslider_id')[:1]
    context ={'settings':settings,'team':team, 'acontent':acontent,'aboutseo':aboutseo,'aboutslider':aboutslider}
    if request.method=="POST":
        emails=request.POST.get('emails')
        en=EmailSubs(emails=emails,)
        en.save()
        messages.success(request, 'You Are Now Our Subscriber')
    return render(request,'about.html',context)
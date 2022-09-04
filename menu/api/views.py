from rest_framework import permissions
from menu.models import breakfastMenu, dinnerMenu, launchMenu, specialMenu
from .serializers import breakfastMenuSerializer, dinnerMenuSerializer, launchMenuSerializer, specialMenuSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def MenuApiUrlOverview(request):
    api_urls = {
        'Breakfas tList':'api/menus/breakfast/',
        'Breakfast Detail View':'api/menus/breakfast/<id>/',
        'Launch List':'api/menus/launch/',
        'Launch Detail View':'api/menus/launch/<id>/',
        'Dinner List':'api/menus/launch/',
        'Dinner Detail View':'api/menus/launch/<id>/',
        'Special Menu List':'api/menus/special/',
        'Special Menu Detail View':'api/menus/special/<id>/',
        
    }
    return Response(api_urls)


#//way for item showing in api//    
#this is best way to ad crud function on django rest api

#Breakfast Menu Content Views for API
class BreakfastMenuList(generics.ListCreateAPIView):
    serializer_class = breakfastMenuSerializer
    
    
    def get_queryset(self):
        queryset = breakfastMenu.objects.all()
        breakfast = self.request.query_params.get('breakfast')
        if breakfast is not None:
            queryset = queryset.filter(breakfastMenu=breakfast)
        return queryset



class BreakfastMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = breakfastMenuSerializer
    queryset = breakfastMenu.objects.all()

#Launch Menu Content Views for API

class launchMenuList(generics.ListCreateAPIView):
    serializer_class = launchMenuSerializer
    
    
    def get_queryset(self):
        queryset = launchMenu.objects.all()
        launch = self.request.query_params.get('launch')
        if launch is not None:
            queryset = queryset.filter(launchMenu=launch)
        return queryset



class launchMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = launchMenuSerializer
    queryset = launchMenu.objects.all()
    
    
    
#Dinner menu Menu Content Views for API

class dinnerMenuList(generics.ListCreateAPIView):
    serializer_class = dinnerMenuSerializer
    
    
    def get_queryset(self):
        queryset = dinnerMenu.objects.all()
        dinner = self.request.query_params.get('dinner')
        if dinner is not None:
            queryset = queryset.filter(launchMenu=dinner)
        return queryset



class dinnerMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = dinnerMenuSerializer
    queryset = dinnerMenu.objects.all()
    
    
    
#Special menu Menu Content Views for API

class specialMenuList(generics.ListCreateAPIView):
    serializer_class = specialMenuSerializer
    
    
    def get_queryset(self):
        queryset = specialMenu.objects.all()
        special = self.request.query_params.get('special')
        if special is not None:
            queryset = queryset.filter(launchMenu=special)
        return queryset



class specialMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = specialMenuSerializer
    queryset = specialMenu.objects.all()
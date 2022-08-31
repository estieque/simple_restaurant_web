from rest_framework import permissions
from about.models import AboutContent, TeamMember
from .serializers import AboutContentSerializer, TeamMemberSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def AboutApiUrlOverview(request):
    api_urls = {
        'List':'api/about/team/',
        'Detail View':'api/about/team/<id>/',
        'AboutApi':'api/about/about/',
        'About Detail':'api/about/about/<id>/',
        
    }
    return Response(api_urls)


#//way for item showing in api//    
#this is best way to ad crud function on django rest api

class teamList(generics.ListCreateAPIView):
    serializer_class = TeamMemberSerializer
    
    
    def get_queryset(self):
        queryset = TeamMember.objects.all()
        team = self.request.query_params.get('team')
        if team is not None:
            queryset = queryset.filter(TeamMember=team)
        return queryset



class teamDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()

#About Content Views for API

class aboutList(generics.ListCreateAPIView):
    serializer_class = AboutContentSerializer
    
    
    def get_queryset(self):
        queryset = AboutContent.objects.all()
        about = self.request.query_params.get('about')
        if about is not None:
            queryset = queryset.filter(aboutList=about)
        return queryset



class aboutDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AboutContentSerializer
    queryset = AboutContent.objects.all()
from rest_framework import permissions
from contact.models import ContactMessage
from .serializers import ContactMessageSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def ContactApiUrlOverview(request):
    api_urls = {
        'List':'api/contact/contact/',
        'Detail View':'api/contact/contact/<id>/',
        
    }
    return Response(api_urls)


#//way for item showing in api//    
#this is best way to ad crud function on django rest api

class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactMessageSerializer
    
    
    def get_queryset(self):
        queryset = ContactMessage.objects.all()
        msg = self.request.query_params.get('msg')
        if msg is not None:
            queryset = queryset.filter(TeamMember=msg)
        return queryset



class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactMessageSerializer
    queryset = ContactMessage.objects.all()

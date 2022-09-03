from rest_framework import permissions
from emailsubs.models import EmailSubs
from .serializers import EmailSubsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def EmailSubsUrlOverview(request):
    api_urls = {
        'List':'api/emailsub/emailsubs/',
        'Detail View':'api/emailsub/emailsubs/<id>/',
        
    }
    return Response(api_urls)


#//way for item showing in api//    
#this is best way to ad crud function on django rest api

class EmailSubsList(generics.ListCreateAPIView):
    serializer_class = EmailSubsSerializer
    
    
    def get_queryset(self):
        queryset = EmailSubs.objects.all()
        emaisubs= self.request.query_params.get('msg')
        if emaisubs is not None:
            queryset = queryset.filter(EmailSubs=emaisubs)
        return queryset



class EmailSubsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmailSubsSerializer
    queryset = EmailSubs.objects.all()

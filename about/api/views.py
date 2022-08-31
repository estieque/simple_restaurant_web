from urllib import response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from about.models import TeamMember
from .serializers import TeamMemberSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from about.api import serializers
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def teamOverview(request):
    api_urls = {
        'List':'/team/',
        'Detail View':'team/<str:pk>/',
    }
    return Response(api_urls)
    

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def team_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = TeamMember.objects.all()
        serializer = TeamMemberSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def team_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        team_detail = TeamMember.objects.get(team_id=pk)
    except TeamMember.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamMemberSerializer(team_detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeamMemberSerializer(team_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from about.models import TeamMember


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
        
        
class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= TeamMember
        fields = ['team_id', 'name', 'phone', 'email', 'image', 'designation',]
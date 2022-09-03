from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from about.models import AboutContent, TeamMember
from contact.models import ContactMessage
from emailsubs.models import EmailSubs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
                

class EmailSubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubs
        fields = ['email_id', 'emails', ]
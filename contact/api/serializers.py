from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from about.models import AboutContent, TeamMember
from contact.models import ContactMessage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
                

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['contact_id', 'name', 'phone', 'email', 'message', 'add_date',]
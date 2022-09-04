from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from about.models import AboutContent, TeamMember
from menu.models import breakfastMenu, dinnerMenu, launchMenu, specialMenu


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
        
        
class breakfastMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model= breakfastMenu
        fields = ['menu_id', 'title', 'price', 'ratings', 'total_reviews', 'image', 'add_date',]
        
        

class breakfastMenuContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = breakfastMenu
        fields = ['menu_id', 'title', 'price', 'ratings', 'total_reviews', 'image', 'add_date',]
        
        
class launchMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model= launchMenu
        fields = ['menu_id', 'title', 'price', 'ratings', 'total_reviews', 'image', 'add_date',]
        
        

class launchMenuContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = breakfastMenu
        fields = ['menu_id', 'title', 'price', 'ratings', 'total_reviews', 'image', 'add_date',]
        
        
        
        
class dinnerMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model= dinnerMenu
        fields = ['menu_id', 'title', 'price', 'ratings', 'total_reviews', 'image', 'add_date',]
        
        

class dinnerMenuContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = dinnerMenu
        fields = ['menu_id', 'title', 'price', 'ratings', 'total_reviews', 'image', 'add_date',]
        
        
        
        
class specialMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model= specialMenu
        fields = ['s_id', 'breakfast', 'launch', 'dinner',]
        
        

class specialMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = specialMenu
        fields = ['s_id', 'breakfast', 'launch', 'dinner',]



from rest_framework import routers
from django.urls import path
from . import views


urlpatterns = [
    path('', views.AboutApiUrlOverview, name="about-api"),
    path('team/', views.teamList.as_view(), name="team"),
    path('team/<str:pk>/', views.teamDetail.as_view(), name="team-details"),
    path('about/', views.aboutList.as_view(), name="aboutUs"),
    path('about/<str:pk>/', views.aboutDetail.as_view(), name="about-content"),
    
]





from rest_framework import routers
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ContactApiUrlOverview, name="contact-api"),
    path('contact/', views.ContactList.as_view(),),
    path('contact/<str:pk>/', views.ContactDetail.as_view(), name="contact-messages"),
    
]


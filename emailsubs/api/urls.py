


from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmailSubsUrlOverview, name="emailsubs-api"),
    path('emailsubs/', views.EmailSubsList.as_view(),),
    path('emailsubs/<str:pk>/', views.EmailSubsDetail.as_view(), name="email-subs"),
    
]


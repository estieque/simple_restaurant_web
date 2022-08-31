


from rest_framework import routers
from django.urls import path, include
from . import views

#router = routers.DefaultRouter()
##router.register(r'team', views.TeamMemberViewSet)
#router.register(r'delete-post', views.DeleteTeamMemberViewSet, basename="delete")

urlpatterns = [
    path('', views.teamOverview, name="team-api"),
    #path('team/', views.teamList, name="team"),
    path('team/', views.team_list, name="team"),
    path('team/<str:pk>/', views.team_detail, name="teamm"),
    #path('team/<str:pk>/', views.teamDetail, name="team-detail"),
    #path('team-create/', views.teamCreate, name="team-create"),
    #path('team-update/<str:pk>/', views.teamUpdate, name="team-update"),
    #path('team-delete/<str:pk>/', views.teamUpdate, name="team-update"),
    
]

#urlpatterns += router.urls

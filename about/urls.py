


from rest_framework import routers
from django.urls import path, include
from . import views

#router = routers.DefaultRouter()
#router.register(r'team', views.TeamMemberViewSet)

urlpatterns = [
    #path('',include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.about, name="about"),
]

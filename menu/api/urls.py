


from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuApiUrlOverview, name="about-api"),
    path('breakfast/', views.BreakfastMenuList.as_view(), name="breakfastmenu"),
    path('breakfast/<str:pk>/', views.BreakfastMenuDetail.as_view(), name="breakfastmenu-details"),
    path('launch/', views.launchMenuList.as_view(), name="launchmenu"),
    path('launch/<str:pk>/', views.launchMenuDetail.as_view(), name="launchmenu-details"),
    path('dinner/', views.dinnerMenuList.as_view(), name="dinnerhmenu"),
    path('dinner/<str:pk>/', views.dinnerMenuDetail.as_view(), name="dinnermenu-details"),
    path('special/', views.specialMenuList.as_view(), name="specialhmenu"),
    path('special/<str:pk>/', views.specialMenuDetail.as_view(), name="specialmenu-details"),
    
]


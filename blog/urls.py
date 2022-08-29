"""cleaningweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path

#admin header customozations
admin.site.site_header = "Crispy Kitchen Dashboard"
admin.site.site_title = "Crispy Kitchen Admin"
admin.site.index_title = "Crispy Kitchen"
#admin header customozations

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<str:slug_url>', views.blog_detail, name="blog_detail")
]

"""restaurant URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('',include('restaurantWeb.urls')),
    path('menu/',include('menu.urls')),
    path('blog/',include('blog.urls')),
    path('reservedone/',include('reservation.urls')),
    path('contact-us/',include('contact.urls')),
    path('about/', include('about.urls')),
#api urls Start from here
    path('api/about/', include('about.api.urls')),
    path('api/contact/', include('contact.api.urls')),
    path('api/emailsub/', include('emailsubs.api.urls')),
    path('api/menus/', include('menu.api.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

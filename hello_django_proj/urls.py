"""hello_django_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from hello_django_app.views import HomePageView
from hello_django_app.views import InfoPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomePageView.as_view(), name = "home_page"),
    path('info/', InfoPageView.as_view(), name = "Info_page"),
    path('', include('hello_django_app.urls')),
 
]

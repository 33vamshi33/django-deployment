"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from app1 import views
from usersapp.views import hello 

urlpatterns = [
    # url(r'^$',views.index,name="index"), url function use
    #path('',views.index,name="index"), using path function
    #url(r'^$',include('app1.urls')),
    path('',include("app1.urls")),
    path('help/',include("help.urls")),
    path('admin/', admin.site.urls),
    path('forms/',include("formapp.urls")),
    path('',include("usersapp.urls")),
    path('hello/',hello,name="hello"),

]

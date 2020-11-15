from django.conf.urls import url
from django.urls import path
from app1 import views

#template tagging compulsary app_name must be used to avoid namescape registration
app_name="app1"

urlpatterns = [

    path('app1/',views.index,name='index'),
    path('releative/',views.releative,name="releative"),
    path('base/',views.base,name="base"),
    
]
